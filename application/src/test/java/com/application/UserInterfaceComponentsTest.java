import com.application.UserInterfaceComponents;
import org.junit.Test;
import static org.junit.Assert.*;

public class UserInterfaceComponentsTest {
    @Test
    public void testCreateComponents() {
        UserInterfaceComponents components = new UserInterfaceComponents();
        assertNotNull(components);
    }
}