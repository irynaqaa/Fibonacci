"""
Selenium Test Script for Validating Output Spectrum Flatness

This script automates the validation of the output spectrum to ensure it is flat across all frequencies
when the volume is set to maximum (0xFF). It includes starting the application, setting the volume,
measuring the output spectrum, and verifying the frequency response.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver

# You can change this to your preferred browser

# Initialize the WebDriver

# You can change this to your preferred browser

driver = webdriver.Chrome()  

try:
    # Step 1: Open the application
    driver.get('http://localhost:5000')  # Adjust the URL as needed

    # Step 2: Set volume to maximum (0xFF)
    volume_slider = driver.find_element(By.ID, 'volume-slider')  # Adjust the selector as needed
    volume_slider.clear()
    volume_slider.send_keys('255')  # Assuming the slider accepts values from 0 to 255

    # Step 3: Trigger measurement of output spectrum
    measure_button = driver.find_element(By.ID, 'measure-button')  # Adjust the selector as needed
    measure_button.click()

    # Step 4: Wait for measurement to complete
    time.sleep(5)  # Adjust the sleep time as needed

    # Step 5: Retrieve and validate the output spectrum
    output_spectrum = driver.find_element(By.ID, 'output-spectrum')  # Adjust the selector as needed
    spectrum_values = output_spectrum.text.split('
')  # Assuming values are separated by new lines

    # Check if the spectrum is flat
    spectrum_values = [float(value) for value in spectrum_values]
    is_flat = all(value == spectrum_values[0] for value in spectrum_values)

    # Validate the flatness of the spectrum
    assert is_flat, "Output spectrum is not flat across all frequencies."
    print("Output spectrum is flat across all frequencies.")

finally:
    # Close the WebDriver
    driver.quit()
