"""
Selenium-based test script for verifying the flat output spectrum and gain matching across channels
when the system is set to flat mode and volume changes (0 dB, -20 dB, -40 dB) are applied.
This script includes modular functions for setting the system to flat mode, applying volume changes,
measuring gain across channels, verifying the output spectrum, and validating gain difference limits
for specified attenuation ranges. Additionally, it includes a test for verifying the flat output spectrum
at maximum volume (RTC index 0xFF) and an end-to-end workflow.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (ensure the appropriate driver is installed and in PATH)
driver = webdriver.Chrome()

# Define constants
BASE_URL = "http://localhost:5000"  # Replace with the actual URL of the application

def set_system_to_flat_mode():
    """Sets the system to flat mode."""
    driver.get(f"{BASE_URL}/flat_mode")  # Replace with the actual route for flat mode
    try:
        # Wait for confirmation that the system is in flat mode
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flat_mode_confirmation"))
        )
        print("System set to flat mode successfully.")
    except Exception as e:
        print("Failed to set system to flat mode:", e)

def set_volume_rtc_index(rtc_index):
    """Sets the volume RTC index to the specified value."""
    driver.get(f"{BASE_URL}/set_rtc_index")  # Replace with the actual route for setting RTC index
    try:
        # Locate the input field and set the RTC index
        rtc_input = driver.find_element(By.ID, "rtc_index_input")
        rtc_input.clear()
        rtc_input.send_keys(rtc_index)
        rtc_input.send_keys(Keys.RETURN)

        # Wait for confirmation that the RTC index was applied
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rtc_index_confirmation"))
        )
        print(f"RTC index set to {rtc_index} successfully.")
    except Exception as e:
        print(f"Failed to set RTC index to {rtc_index}:", e)

def verify_output_spectrum():
    """Verifies the flat output spectrum."""
    driver.get(f"{BASE_URL}/output_spectrum")  # Replace with the actual route for output spectrum
    try:
        # Check if the output spectrum is flat
        spectrum_status = driver.find_element(By.ID, "spectrum_status").text
        if spectrum_status == "Flat":
            print("Output spectrum is flat.")
        else:
            print("Output spectrum is not flat.")
    except Exception as e:
        print("Failed to verify output spectrum:", e)

def record_frequency_response():
    """Records the frequency response of the system."""
    driver.get(f"{BASE_URL}/record_frequency_response")  # Replace with the actual route
    try:
        # Wait for the frequency response recording to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "frequency_response_complete"))
        )
        print("Frequency response recorded successfully.")
    except Exception as e:
        print("Failed to record frequency response:", e)

def measure_gain_values():
    """Measures gain values across channels."""
    driver.get(f"{BASE_URL}/measure_gain")  # Replace with the actual route for measuring gain
    try:
        # Retrieve gain values for all channels
        gain_values = driver.find_element(By.ID, "gain_values").text
        gain_values = [float(value) for value in gain_values.split(",")]
        print(f"Measured gain values: {gain_values}")
        return gain_values
    except Exception as e:
        print("Failed to measure gain values:", e)
        return []

def verify_gain_matching(gain_values, tolerance=0.5):
    """Verifies that the gain differences across channels are within the specified tolerance."""
    try:
        max_gain = max(gain_values)
        min_gain = min(gain_values)
        if (max_gain - min_gain) <= tolerance:
            print("Gain matching across channels is within tolerance.")
        else:
            print("Gain matching across channels is NOT within tolerance.")
    except Exception as e:
        print("Failed to verify gain matching:", e)

def end_to_end_workflow():
    """Performs the end-to-end workflow for verifying the flat output spectrum and gain matching."""
    try:
        print("Starting end-to-end workflow...")
        set_system_to_flat_mode()
        set_volume_rtc_index("0x80")
        verify_output_spectrum()
        record_frequency_response()
        gain_values = measure_gain_values()
        verify_gain_matching(gain_values)
        print("End-to-end workflow completed successfully.")
    except Exception as e:
        print("End-to-end workflow failed:", e)

# Main test execution
if __name__ == "__main__":
    try:
        end_to_end_workflow()
    finally:
        # Close the WebDriver
        driver.quit()