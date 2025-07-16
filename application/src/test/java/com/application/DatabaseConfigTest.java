import com.application.DatabaseConfig;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class DatabaseConfigTest {
    @Autowired
    private DatabaseConfig config;

    @Test
    public void testDataSource() {
        // Add test data
        // Assert that the data source is not null
        assertNotNull(config.dataSource());
    }
}
