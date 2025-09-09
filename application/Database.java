import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Database {
    private static final String DB_URL = "jdbc:sqlite:expenses.db";

    public static void createTable() {
        String query = "CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                customer_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                transaction_date TEXT NOT NULL
        );";

        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.execute();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void insertTransaction(Transaction transaction) {
        String query = "INSERT INTO transactions(amount, customer_id, transaction_type, transaction_date) VALUES(?,?,?,?)";

        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement stmt = conn.prepareStatement(query)) {

            stmt.setDouble(1, transaction.getAmount());
            stmt.setInt(2, transaction.getCustomerID());
            stmt.setString(3, transaction.getTransactionType());
            stmt.setString(4, transaction.getTransactionDate());

            stmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void selectTransactions() {
        String query = "SELECT * FROM transactions";

        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement stmt = conn.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getDouble("amount") + " " + rs.getInt("customer_id") + " " + rs.getString("transaction_type") + " " + rs.getString("transaction_date"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}