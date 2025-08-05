import org.junit.Test;
import static org.junit.Assert.*;
import com.example.personal.expense.tracker.DatabaseManager;

public class DatabaseManagerTest {
    @Test
    public void testSaveDataPersistently() {
        // Test saving data persistently using SQLite
        DatabaseManager databaseManager = new DatabaseManager();
        databaseManager.saveData("Data");
        assertTrue(databaseManager.dataSaved());
    }
}
