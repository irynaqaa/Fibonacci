import com.application.ExpenseTrackerRepository;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ExpenseTrackerRepositoryTest {
    @Autowired
    private ExpenseTrackerRepository repository;

    @Test
    public void testFindAll() {
        // Add test data
        // Assert that the result is not empty
        assertNotNull(repository.findAll());
    }
}
