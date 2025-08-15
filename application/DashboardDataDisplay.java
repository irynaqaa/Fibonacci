import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DashboardDataDisplay {
    private Connection connection;

    public DashboardDataDisplay(String databaseLocation) {
        try {
            Class.forName("org.sqlite.JDBC");
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databaseLocation);
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void displayData() {
        String query = "SELECT * FROM transactions";
        try (Statement statement = this.connection.createStatement(); ResultSet resultSet = statement.executeQuery(query)) {
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String type = resultSet.getString("type");
                double amount = resultSet.getDouble("amount");
                String date = resultSet.getString("date");
                System.out.println("ID: " + id + ", Type: " + type + ", Amount: " + amount + ", Date: " + date);
            }
        } catch (SQLException e) {
            System.out.println("Error displaying data: " + e.getMessage());
        }
    }

    public void displaySummary() {
        String query = "SELECT SUM(amount) AS total FROM transactions WHERE type = 'income'";
        try (Statement statement = this.connection.createStatement(); ResultSet resultSet = statement.executeQuery(query)) {
            double totalIncome = resultSet.getDouble("total");
            query = "SELECT SUM(amount) AS total FROM transactions WHERE type = 'expense'";
            try (Statement statement2 = this.connection.createStatement(); ResultSet resultSet2 = statement2.executeQuery(query)) {
                double totalExpense = resultSet2.getDouble("total");
                double balance = totalIncome - totalExpense;
                System.out.println("Total Income: " + totalIncome);
                System.out.println("Total Expense: " + totalExpense);
                System.out.println("Balance: " + balance);
            }
        } catch (SQLException e) {
            System.out.println("Error displaying summary: " + e.getMessage());
        }
    }

    public void closeConnection() {
        try {
            this.connection.close();
        } catch (SQLException e) {
            System.out.println("Error closing database connection: " + e.getMessage());
        }
    }
}