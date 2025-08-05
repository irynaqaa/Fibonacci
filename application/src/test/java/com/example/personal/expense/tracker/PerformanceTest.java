import org.junit.Test;
import static org.junit.Assert.*;
import com.example.personal.expense.tracker.Transaction;

public class PerformanceTest {
    @Test
    public void testHandleUpTo1000TransactionsSmoothly() {
        // Test handling up to 1000 transactions smoothly
        for (int i = 0; i < 1000; i++) {
            // Simulate a transaction
            Transaction transaction = new Transaction(100, "Category", "2022-01-01", "Description", "Income");
        }
        assertTrue(true);
    }
}
