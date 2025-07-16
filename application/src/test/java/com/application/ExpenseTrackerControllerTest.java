import com.application.ExpenseTrackerController;
import org.junit.Test;
import static org.junit.Assert.*;

public class ExpenseTrackerControllerTest {
    @Test
    public void testLogin() {
        ExpenseTrackerController controller = new ExpenseTrackerController();
        boolean result = controller.login("username", "password");
        assertTrue(result);
    }
}
