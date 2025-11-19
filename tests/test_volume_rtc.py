import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def setup_module():
    """Setup for the Selenium WebDriver."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_gain_matching_across_channels(setup_module):
    """Test for Gain Matching Across Channels"""
    driver = setup_module
    # Navigate to the application
    driver.get("http://localhost:5000")  # Adjust the URL as necessary

    # Set the volume levels for both channels
    channel1_volume = driver.find_element(By.ID, 'channel1_volume')
    channel1_volume.clear()
    channel1_volume.send_keys('0')

    channel2_volume = driver.find_element(By.ID, 'channel2_volume')
    channel2_volume.clear()
    channel2_volume.send_keys('-20')

    time.sleep(2)  # Wait for the application to process the input

    # Measure the gain values
    gain1 = float(driver.find_element(By.ID, 'gain_channel1').text)
    gain2 = float(driver.find_element(By.ID, 'gain_channel2').text)

    # Assert that the gain difference does not exceed 1.0 dB
    assert abs(gain1 - gain2) <= 1.0, f"Gain difference exceeds limit: {abs(gain1 - gain2)} dB"

    # Verify initial state
    initial_spectrum = driver.find_element(By.ID, "spectrum_output").text
    assert "expected_initial_value" in initial_spectrum  # Replace with actual expected value

    # Change volume RTC index to 0x80
    volume_input = driver.find_element(By.ID, "volume_rtc_index")
    volume_input.clear()
    volume_input.send_keys("128")  # 0x80 in decimal
    driver.find_element(By.ID, "set_volume_button").click()

    # Wait for the output spectrum to update
    time.sleep(2)  # Adjust sleep time as necessary

    # Measure the output spectrum
    updated_spectrum = driver.find_element(By.ID, "spectrum_output").text
    assert "expected_updated_value" in updated_spectrum  # Replace with actual expected value

    # Validate results
    assert updated_spectrum != initial_spectrum, "Output spectrum did not change after volume RTC index update."
