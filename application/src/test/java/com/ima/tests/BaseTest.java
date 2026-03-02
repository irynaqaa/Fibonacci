// Base test class for initializing WebDriver and common setup

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class BaseTest {
    protected WebDriver driver;

    // Setup method to initialize WebDriver
    @BeforeEach
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
    }

    // Teardown method to close WebDriver
    @AfterEach
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}