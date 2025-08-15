import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class TransactionDAO {
    private Connection connection;

    public TransactionDAO(String databaseLocation) {
        try {
            Class.forName("org.sqlite.JDBC");
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databaseLocation);
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public List<Transaction> getTransactions() {
        List<Transaction> transactions = new ArrayList<>();
        String query = "SELECT * FROM transactions";
        try (Statement statement = this.connection.createStatement(); ResultSet resultSet = statement.executeQuery(query)) {
            while (resultSet.next()) {
                Transaction transaction = new Transaction();
                transaction.setId(resultSet.getInt("id"));
                transaction.setType(resultSet.getString("type"));
                transaction.setAmount(resultSet.getDouble("amount"));
                transaction.setDate(resultSet.getString("date"));
                transactions.add(transaction);
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving transactions: " + e.getMessage());
        }
        return transactions;
    }

    public void addTransaction(Transaction transaction) {
        String query = "INSERT INTO transactions (type, amount, date) VALUES (?, ?, ?)";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, transaction.getType());
            statement.setDouble(2, transaction.getAmount());
            statement.setString(3, transaction.getDate());
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error adding transaction: " + e.getMessage());
        }
    }

    public void updateTransaction(Transaction transaction) {
        String query = "UPDATE transactions SET type = ?, amount = ?, date = ? WHERE id = ?";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, transaction.getType());
            statement.setDouble(2, transaction.getAmount());
            statement.setString(3, transaction.getDate());
            statement.setInt(4, transaction.getId());
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error updating transaction: " + e.getMessage());
        }
    }

    public void deleteTransaction(int id) {
        String query = "DELETE FROM transactions WHERE id = ?";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setInt(1, id);
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error deleting transaction: " + e.getMessage());
        }
    }
}