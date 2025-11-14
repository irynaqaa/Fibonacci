import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import fibonacci_module as fb

####    Tests for Fibonacci Numbers    ####

#### Sample inputs for list of Fibonacci numbers ####
print ("Sample inputs for list of Fibonacci numbers")
print ("  n=0:   ", fb.fibList(0))
print ("  n=1:   ", fb.fibList(1))
print ("  n=2:   ", fb.fibList(2))
print ("  n=3.2: ", fb.fibList(3.2))
print ("  n=4.9: ", fb.fibList(4.9))
print ("  n=5:   ", fb.fibList(5))
print ("  n=15:  ", fb.fibList(15))
print ("  n=100: ", fb.fibList(100))

print ("
Intentionally using invalid inputs")
print ("  n=-1: ", fb.fibList(-1))
print ("  n=foo: ", fb.fibList("foo"))

####    Selenium Test for Flat Output Spectrum    ####

def test_flat_output_spectrum():
    # 1. Start the application
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://localhost:5000")  # Adjust URL as necessary

    # 2. Set the volume RTC index to 0x80
    volume_control = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "volume_control_id"))  # Replace with actual ID
    )
    volume_control.send_keys("0x80")

    # 3. Measure output spectrum (this part may require additional implementation)
    measure_button = driver.find_element(By.ID, "measure_button_id")  # Replace with actual ID
    measure_button.click()

    # 4. Validate the output spectrum (this part may require additional implementation)
    # Add logic to validate the output spectrum here

    driver.quit()


if __name__ == '__main__':
    test_flat_output_spectrum()