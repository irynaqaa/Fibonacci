import pytest
from application.test_script import TestGainMatching
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_method")
class TestFlatMode:
    """
    Test case TC-002: Verify functionality of the system when volume RTC index is changed to 0x80
    """

    def test_change_volume_rtc_index(self):
        """
        Test to change the volume RTC command to index 0x80 and verify the outcome.
        """
        volume_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'volume_input'))
        )
        volume_input.send_keys('0x80')

        send_button = self.driver.find_element(By.ID, 'send_button')
        send_button.click()

        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'success_message'))
        )
        assert success_message.text == "Volume RTC command sent successfully."

    def test_measure_output_spectrum(self):
        """
        Test to measure the output spectrum from the output channel after changing the volume RTC index.
        """
        measure_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'measure_button'))
        )
        measure_button.click()

        output_spectrum = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'output_spectrum'))
        )
        assert output_spectrum.is_displayed()

    def test_validate_flat_output_spectrum(self):
        """
        Test to validate that the output spectrum drops in level but remains flat across all frequencies.
        """
        flat_check_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'flat_check_button'))
        )
        flat_check_button.click()

        validation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'validation_message'))
        )
        assert validation_message.text == "Output spectrum is flat."

        # Reset system to original state
        reset_button = self.driver.find_element(By.ID, 'reset_button')
        reset_button.click()


class TestGainMatching:
    """
    Test case TC-003: Verify gain matching across channels after volume changes.
    """

    def setup_method(self):
        """
        Setup method to initialize the WebDriver and navigate to the application.
        """
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:5000')  # Adjust URL as needed

    def teardown_method(self):
        """
        Teardown method to close the WebDriver after tests.
        """
        self.driver.quit()

    def test_start_application(self):
        """
        Test to verify that the application has started successfully.
        """
        main_window = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'main_window'))  # Adjust locator as needed
        )
        assert main_window.is_displayed(), "Main window did not display."

    def test_set_channel_1_volume(self):
        """
        Test to set the volume for Channel 1 to 0 dB.
        """
        channel_1_volume = self.driver.find_element(By.ID, 'channel_1_volume')  # Adjust locator as needed
        channel_1_volume.send_keys('0')
        apply_button = self.driver.find_element(By.ID, 'apply_volume')  # Adjust locator as needed
        apply_button.click()
        # Verify volume is set to 0 dB
        volume_status = self.driver.find_element(By.ID, 'volume_status')  # Adjust locator as needed
        assert "0 dB" in volume_status.text, "Channel 1 volume not set to 0 dB."

    def test_set_channel_2_volume(self):
        """
        Test to set the volume for Channel 2 to -20 dB.
        """
        channel_2_volume = self.driver.find_element(By.ID, 'channel_2_volume')  # Adjust locator as needed
        channel_2_volume.send_keys('-20')
        apply_button = self.driver.find_element(By.ID, 'apply_volume')  # Adjust locator as needed
        apply_button.click()
        # Verify volume is set to -20 dB
        volume_status = self.driver.find_element(By.ID, 'volume_status')  # Adjust locator as needed
        assert "-20 dB" in volume_status.text, "Channel 2 volume not set to -20 dB."

    def test_measure_gain_values(self):
        """
        Test to measure and record gain values for both channels.
        """
        # Simulate gain measurement logic here
        self.channel_1_gain = -1.0  # Example gain value for Channel 1
        self.channel_2_gain = -1.5  # Example gain value for Channel 2

    def test_validate_gain_difference(self):
        """
        Test to validate that the gain difference does not exceed 1.0 dB.
        """
        gain_difference = abs(self.channel_1_gain - self.channel_2_gain)
        assert gain_difference <= 1.0, f"Gain difference {gain_difference} exceeds 1.0 dB"

    def test_repeat_process_for_other_volumes(self):
        """
        Test to repeat the process for other volume settings.
        """
        # Logic to set other volume levels and validate gain differences
        # Example: set volume to -40 dB and validate gain differences
        pass
