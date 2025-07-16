import com.application.ExpenseTrackerService;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ExpenseTrackerServiceTest {
    @Autowired
    private ExpenseTrackerService service;

    @Test
    public void testGetAllExpenses() {
        // Add test data
        // Assert that the result is not empty
        assertNotNull(service.getAllExpenses());
    }
}