import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * AnotherService class that handles different operations.
 */
public class AnotherService {
    private static final Logger logger = LoggerFactory.getLogger(AnotherService.class);

    public void executeTask() {
        logger.info("Executing task...");
        // Task logic here
        logger.info("Task executed successfully.");
    }
}