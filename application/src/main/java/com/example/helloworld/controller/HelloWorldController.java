import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * This is the controller class for the Spring Boot application.
 */
@RestController
public final class HelloWorldController {

    /**
     * This method handles the GET request to the root URL and returns a hello message.
     * @return A hello message.
     */
    @GetMapping("/")
    public String helloWorld() {
        return "Hello World!";
    }

}