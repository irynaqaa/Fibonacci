"""
Selenium-based test automation for verifying the flat output spectrum in flat mode.
This script follows the Page Object Model (POM) structure for efficient test execution.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class FlatModePage:
    """
    Page Object Model for the Flat Mode functionality.
    """

    def __init__(self, driver):
        self.driver = driver
        self.flat_mode_button = (By.ID, "flatModeButton")
        self.volume_rtc_input = (By.ID, "volumeRTCInput")
        self.frequency_sweep_button = (By.ID, "frequencySweepButton")
        self.output_spectrum = (By.ID, "outputSpectrum")
        self.input_channel_activity = (By.ID, "inputChannelActivity")

    def set_flat_mode(self):
        """Set the system to flat mode."""
        flat_mode_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.flat_mode_button)
        )
        flat_mode_btn.click()

    def send_volume_rtc_command(self, rtc_value):
        """Send the volume RTC command."""
        volume_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.volume_rtc_input)
        )
        volume_input.clear()
        volume_input.send_keys(rtc_value)
        volume_input.send_keys(Keys.RETURN)

    def initiate_frequency_sweep(self):
        """Initiate a frequency sweep."""
        sweep_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.frequency_sweep_button)
        )
        sweep_button.click()

    def measure_output_spectrum(self):
        """Measure the output spectrum."""
        spectrum = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.output_spectrum)
        )
        return spectrum.text

    def validate_input_channel_activity(self):
        """Validate input channel activity."""
        activity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.input_channel_activity)
        )
        return activity.text


def test_flat_mode():
    """
    Test case for verifying the flat output spectrum in flat mode.
    """
    # Configure WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    service = Service("/path/to/chromedriver")  # Update with the correct path to chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the application
        driver.get("http://localhost:5000")  # Update with the correct URL of the application

        # Initialize the FlatModePage
        flat_mode_page = FlatModePage(driver)

        # Perform the test steps
        flat_mode_page.set_flat_mode()
        flat_mode_page.send_volume_rtc_command("0xFF")
        flat_mode_page.initiate_frequency_sweep()

        # Validate the output spectrum
        output_spectrum = flat_mode_page.measure_output_spectrum()
        print("Output Spectrum:", output_spectrum)

        # Validate input channel activity
        input_activity = flat_mode_page.validate_input_channel_activity()
        print("Input Channel Activity:", input_activity)

        # Add assertions as needed
        assert "Flat" in output_spectrum, "Output spectrum is not flat!"
        assert "Active" in input_activity, "Input channel is not active!"

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    test_flat_mode()