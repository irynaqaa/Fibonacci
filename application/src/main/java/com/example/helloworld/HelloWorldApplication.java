import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * This is the main application class for the Spring Boot application.
 */
@SpringBootApplication
public class HelloWorldApplication {

    /**
     * This is the main method that runs the Spring Boot application.
     * @param args Command line arguments.
     */
    public static void main(final String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }

}