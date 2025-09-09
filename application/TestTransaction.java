import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestTransaction {
    @Test
    public void testTransaction() {
        Transaction transaction = new Transaction(100, "Category", "2022-01-01", "Description", "Income");
        assertEquals(100, transaction.getAmount(), 0);
        assertEquals("Category", transaction.getCategory());
        assertEquals("2022-01-01", transaction.getDate());
        assertEquals("Description", transaction.getDescription());
        assertEquals("Income", transaction.getType());
    }
}