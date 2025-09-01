import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Logger class to handle logging throughout the application.
 */
public class Logger {
    private static final Logger logger = LoggerFactory.getLogger(Logger.class);

    public static void info(String message) {
        logger.info(message);
    }

    public static void error(String message) {
        logger.error(message);
    }

    public static void debug(String message) {
        logger.debug(message);
    }

    public static void warn(String message) {
        logger.warn(message);
    }
}