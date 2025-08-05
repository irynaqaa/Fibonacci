import org.junit.Test;
import static org.junit.Assert.*;
import com.example.personal.expense.tracker.ReportGenerator;

public class ReportGeneratorTest {
    @Test
    public void testGenerateMonthlySummary() {
        // Test generating a monthly summary
        ReportGenerator reportGenerator = new ReportGenerator();
        String monthlySummary = reportGenerator.generateMonthlySummary("2022-01");
        assertNotNull(monthlySummary);
    }
}
