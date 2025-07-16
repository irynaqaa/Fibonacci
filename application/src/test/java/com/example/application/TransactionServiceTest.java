import com.example.application.TransactionService;
import com.example.application.Transaction;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TransactionServiceTest {
    @Test
    public void testAddTransaction() {
        TransactionService service = new TransactionService();
        Transaction transaction = new Transaction();
        transaction.setAmount(100.0);
        transaction.setCategory("Test Category");
        transaction.setDate(new Date());
        transaction.setDescription("Test Description");
        service.addTransaction(transaction);
        assertEquals(1, service.getTransactions().size());
    }
}
