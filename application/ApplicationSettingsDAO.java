import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ApplicationSettingsDAO {
    private Connection connection;

    public ApplicationSettingsDAO(String databaseLocation) {
        try {
            Class.forName("org.sqlite.JDBC");
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databaseLocation);
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public ApplicationSettings getApplicationSettings() {
        ApplicationSettings settings = new ApplicationSettings();
        String query = "SELECT * FROM application_settings";
        try (Statement statement = this.connection.createStatement(); ResultSet resultSet = statement.executeQuery(query)) {
            while (resultSet.next()) {
                settings.setDatabaseLocation(resultSet.getString("database_location"));
                settings.setCSVExportLocation(resultSet.getString("csv_export_location"));
            }
        } catch (SQLException e) {
            System.out.println("Error retrieving application settings: " + e.getMessage());
        }
        return settings;
    }

    public void updateApplicationSettings(ApplicationSettings settings) {
        String query = "UPDATE application_settings SET database_location = ?, csv_export_location = ?";
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, settings.getDatabaseLocation());
            statement.setString(2, settings.getCSVExportLocation());
            statement.execute();
        } catch (SQLException e) {
            System.out.println("Error updating application settings: " + e.getMessage());
        }
    }
}