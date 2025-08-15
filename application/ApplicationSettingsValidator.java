import java.util.regex.Pattern;

public class ApplicationSettingsValidator {
    public boolean isValidDatabaseLocation(String location) {
        // Check if the location is a valid file path
        if (location == null || location.isEmpty()) {
            return false;
        }
        return true;
    }

    public boolean isValidCSVExportLocation(String location) {
        // Check if the location is a valid file path
        if (location == null || location.isEmpty()) {
            return false;
        }
        return true;
    }
}