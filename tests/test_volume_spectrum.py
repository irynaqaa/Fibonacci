import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestVolumeSpectrum:
    """
    Test class to verify gain values consistency across channels after volume changes.
    """

    @pytest.fixture(scope="class")
    def setup_class(cls):
        """
        Setup method to initialize the Chrome WebDriver.
        """
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("http://localhost:5000")  # Adjust the URL as needed
        yield
        cls.driver.quit()

    def test_gain_values_consistency(self, setup_class):
        """
        Test to verify that gain values remain consistent across channels after volume changes.
        """
        # Set volume for channel 1
        self.driver.find_element(By.ID, "volume_channel_1").send_keys("80")
        time.sleep(1)  # Wait for the application to process the input

        # Set volume for channel 2
        self.driver.find_element(By.ID, "volume_channel_2").send_keys("80")
        time.sleep(1)  # Wait for the application to process the input

        # Measure gain values
        gain_channel_1 = float(self.driver.find_element(By.ID, "gain_channel_1").text)
        gain_channel_2 = float(self.driver.find_element(By.ID, "gain_channel_2").text)

        # Validate gain difference
        gain_difference = abs(gain_channel_1 - gain_channel_2)
        assert gain_difference <= 0.5, f"Gain difference {gain_difference} exceeds limit"  # Adjust limit as needed
