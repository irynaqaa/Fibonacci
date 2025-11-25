import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestGainMatching:
    """
    Test class to verify that the output spectrum remains flat after applying gain changes.
    """

    @pytest.fixture(scope="class")
    def setup_class(cls):
        """
        Setup method to initialize the Chrome WebDriver.
        """
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("http://localhost:5000/")  # Start the application
        yield
        cls.driver.quit()

    def test_gain_matching(self, setup_class):
        """
        Test to set volume levels and verify output spectrum.
        """
        # Set volume for Channel 1 to -40 dB
        channel_1_volume = self.driver.find_element(By.ID, "channel_1_volume")
        channel_1_volume.clear()
        channel_1_volume.send_keys("-40")

        # Set volume for Channel 2 to -20 dB
        channel_2_volume = self.driver.find_element(By.ID, "channel_2_volume")
        channel_2_volume.clear()
        channel_2_volume.send_keys("-20")

        # Apply the changes
        apply_button = self.driver.find_element(By.ID, "apply_button")
        apply_button.click()

        # Wait for the output spectrum to be updated
        time.sleep(2)  # Adjust sleep time as necessary

        # Measure the output spectrum
        output_spectrum = self.driver.find_element(By.ID, "output_spectrum")
        spectrum_values = output_spectrum.text.split()  # Assuming values are space-separated

        # Validate that the output spectrum is flat
        assert self.is_flat_spectrum(spectrum_values), "Output spectrum is not flat."

    def is_flat_spectrum(self, spectrum_values):
        """
        Helper method to check if the spectrum values are flat.
        """
        # Convert string values to float
        spectrum_values = list(map(float, spectrum_values))
        return all(abs(spectrum_values[i] - spectrum_values[i + 1]) < 0.1 for i in range(len(spectrum_values) - 1))


if __name__ == "__main__":
    pytest.main()