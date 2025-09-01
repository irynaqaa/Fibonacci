import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * MainApplication class to run the application.
 */
public class MainApplication {
    private static final Logger logger = LoggerFactory.getLogger(MainApplication.class);

    public static void main(String[] args) {
        logger.info("Application is starting...");
        SomeService service = new SomeService();
        service.performOperation();
        AnotherService anotherService = new AnotherService();
        anotherService.executeTask();
        logger.info("Application has finished running.");
    }
}