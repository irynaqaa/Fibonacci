import org.junit.Test;
import static org.junit.Assert.*;
import com.example.personal.expense.tracker.Transaction;

public class TransactionTest {
    @Test
    public void testAddTransaction() {
        // Test adding a new transaction with valid input
        Transaction transaction = new Transaction(100, "Category", "2022-01-01", "Description", "Income");
        assertEquals(100, transaction.getAmount(), 0);
        assertEquals("Category", transaction.getCategory());
        assertEquals("2022-01-01", transaction.getDate());
        assertEquals("Description", transaction.getDescription());
        assertEquals("Income", transaction.getType());
    }

    @Test
    public void testAddTransactionInvalidInput() {
        // Test adding a new transaction with invalid input (negative amount)
        try {
            new Transaction(-100, "Category", "2022-01-01", "Description", "Income");
            fail("Expected exception not thrown");
        } catch (Exception e) {
            assertEquals("Invalid amount", e.getMessage());
        }
    }
}
