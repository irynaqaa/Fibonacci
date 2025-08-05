import org.junit.Test;
import static org.junit.Assert.*;
import com.example.personal.expense.tracker.Category;

public class CategoryTest {
    @Test
    public void testChooseFromPredefinedCategories() {
        // Test choosing from predefined categories
        Category category = new Category("Food");
        assertEquals("Food", category.getName());
    }

    @Test
    public void testCreateCustomCategory() {
        // Test creating a custom category
        Category category = new Category("Custom Category");
        assertEquals("Custom Category", category.getName());
    }
}
