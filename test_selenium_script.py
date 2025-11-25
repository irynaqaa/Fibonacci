import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestGainMatching(unittest.TestCase):
    """
    Selenium test case to verify gain matching across channels after volume changes.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the Selenium WebDriver.
        """
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get('http://localhost:5000')  # Adjust the URL as needed

    def test_gain_matching(self):
        """
        Test to set the volume for Channel 1 to 0 dB and Channel 2 to -20 dB, and verify gain values.
        """
        # Set volume for Channel 1 to 0 dB
        channel_1_volume = self.driver.find_element(By.ID, 'channel_1_volume')
        channel_1_volume.clear()
        channel_1_volume.send_keys('0')

        # Set volume for Channel 2 to -20 dB
        channel_2_volume = self.driver.find_element(By.ID, 'channel_2_volume')
        channel_2_volume.clear()
        channel_2_volume.send_keys('-20')

        # Submit the volume settings
        submit_button = self.driver.find_element(By.ID, 'submit_volumes')
        submit_button.click()

        # Wait for the gain values to be updated
        time.sleep(2)  # Adjust sleep time as necessary

        # Measure and record the gain values
        gain_channel_1 = float(self.driver.find_element(By.ID, 'gain_channel_1').text)
        gain_channel_2 = float(self.driver.find_element(By.ID, 'gain_channel_2').text)

        # Validate that the gain difference does not exceed specified limits
        gain_difference = abs(gain_channel_1 - gain_channel_2)
        self.assertLessEqual(gain_difference, 1.0, f'Gain difference exceeded: {gain_difference} dB')

    @classmethod
    def tearDownClass(cls):
        """
        Close the Selenium WebDriver.
        """
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()  
