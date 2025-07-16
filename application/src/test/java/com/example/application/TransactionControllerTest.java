import com.example.application.TransactionController;
import com.example.application.Transaction;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TransactionControllerTest {
    @Test
    public void testAddTransaction() {
        TransactionController controller = new TransactionController();
        Transaction transaction = new Transaction();
        transaction.setAmount(100.0);
        transaction.setCategory("Test Category");
        transaction.setDate(new Date());
        transaction.setDescription("Test Description");
        controller.addTransaction(transaction);
        assertEquals(1, controller.getTransactions().size());
    }
}
