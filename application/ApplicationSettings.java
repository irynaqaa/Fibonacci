import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ApplicationSettings {
    private String databaseLocation;
    private String csvExportLocation;

    public ApplicationSettings() {
        this.databaseLocation = "";
        this.csvExportLocation = "";
    }

    public void setDatabaseLocation(String location) {
        this.databaseLocation = location;
    }

    public void setCSVExportLocation(String location) {
        this.csvExportLocation = location;
    }

    public String getDatabaseLocation() {
        return this.databaseLocation;
    }

    public String getCSVExportLocation() {
        return this.csvExportLocation;
    }

    public void saveSettings() {
        try (FileWriter writer = new FileWriter("application_settings.txt")) {
            writer.write("Database Location: " + this.databaseLocation + "
");
            writer.write("CSV Export Location: " + this.csvExportLocation + "
");
        } catch (IOException e) {
            System.out.println("Error saving settings: " + e.getMessage());
        }
    }

    public void loadSettings() {
        try (Scanner scanner = new Scanner(new File("application_settings.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.startsWith("Database Location:")) {
                    this.databaseLocation = line.split(":")[1].trim();
                } else if (line.startsWith("CSV Export Location:")) {
                    this.csvExportLocation = line.split(":")[1].trim();
                }
            }
        } catch (IOException e) {
            System.out.println("Error loading settings: " + e.getMessage());
        }
    }
}
