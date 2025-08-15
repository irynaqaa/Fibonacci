import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class CreateDB {
    public void createDatabase(String databaseLocation) {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:" + databaseLocation)) {
            String query = "CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )";
            try (Statement statement = connection.createStatement()) {
                statement.execute(query);
            }

            query = "CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )";
            try (Statement statement = connection.createStatement()) {
                statement.execute(query);
            }
        } catch (SQLException e) {
            System.out.println("Error creating database: " + e.getMessage());
        }
    }
}