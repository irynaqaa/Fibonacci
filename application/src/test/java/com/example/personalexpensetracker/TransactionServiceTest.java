import com.example.personalexpensetracker.TransactionService;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import com.example.personalexpensetracker.Transaction;

public class TransactionServiceTest {
    @Test
    public void testAddTransaction() {
        // Given
        TransactionService transactionService = new TransactionService();
        Transaction transaction = new Transaction("2022-01-01", "Food", 10.99, "Lunch");
        
        // When
        transactionService.addTransaction(transaction);
        
        // Then
        assertEquals(1, transactionService.getTransactions().size());
    }
}