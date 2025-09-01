import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * SomeService class that performs some operations.
 */
public class SomeService {
    private static final Logger logger = LoggerFactory.getLogger(SomeService.class);

    public void performOperation() {
        logger.info("Performing operation...");
        // Operation logic here
        logger.info("Operation completed successfully.");
    }
}