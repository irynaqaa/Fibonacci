import com.example.application.TransactionRepository;
import com.example.application.Transaction;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TransactionRepositoryTest {
    @Test
    public void testAddTransaction() {
        TransactionRepository repository = new TransactionRepository();
        Transaction transaction = new Transaction();
        transaction.setAmount(100.0);
        transaction.setCategory("Test Category");
        transaction.setDate(new Date());
        transaction.setDescription("Test Description");
        repository.addTransaction(transaction);
        assertEquals(1, repository.getTransactions().size());
    }
}
