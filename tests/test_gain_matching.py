import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_gain_matching():
    """
    Test to verify the gain matching functionality of the application.
    This includes setting the gain, sending a command, and verifying the response.
    """
    # Setup WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:5000')  # URL of the application

    # Wait for the main interface to load
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "main_interface")))  # Adjust locator as needed

    # Set the gain value
    gain_input = driver.find_element(By.ID, "gain_input")  # Adjust locator as needed
    gain_input.clear()
    gain_input.send_keys("10")  # Set gain to 10
    set_gain_button = driver.find_element(By.ID, "set_gain_button")  # Adjust locator as needed
    set_gain_button.click()

    # Verify the gain has been set
    assert "Gain set to 10" in driver.page_source  # Verify gain setting response

    driver.quit()


if __name__ == '__main__':
    pytest.main()