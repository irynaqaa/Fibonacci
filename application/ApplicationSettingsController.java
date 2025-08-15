import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class ApplicationSettingsController {
    private ApplicationSettingsDAO dao;

    public ApplicationSettingsController() {
        this.dao = new ApplicationSettingsDAO();
    }

    public void saveSettings(ApplicationSettings settings) {
        dao.saveSettings(settings);
    }

    public ApplicationSettings loadSettings() {
        return dao.loadSettings();
    }
}