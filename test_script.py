import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_gain_matching():
    """Test for Gain Matching Across Channels"""
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run headless Chrome
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Start the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the application
        driver.get('http://localhost:5000')

        # Wait for the page to load
        time.sleep(2)

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

    finally:
        # Close the driver
        driver.quit()


if __name__ == '__main__':
    test_gain_matching()

####    Tests for Fibonacci Numbers    ####
import fibonacci_module as fb
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

####    Tests for Square Numbers    ####
print ("
Tests for is_square function:")
testList = [0, 1, 2, 3, 4, +8, +9, 16, 25.0, 120.9999999, 1e4]
print("  Number   Perfect Square?")
for val in testList:
    print("  ", val, "      ", fb.is_square(val))
## Stuff that should error
#print("  -9", fb.is_square(-9))
#print(" foo", fb.is_square("foo"))


####    Tests for Is_Fibonacci    ####
print ("
Tests for is_fibonacci function:")
testList = [0, 1, 2, 3, 4, 5, 12, 13, 42, 218922995834555169026]
testList = [(0, "Y"), (1, "Y"), (2, "Y"), (3, "Y"), (4, "N"), (5, "Y"), (12, "N"), (13, "Y"), (42, "N"), (144, "Y"), (63245986,"Y"), (102334155, "Y"), (218922995834555169026, "Y")]  
print("  Number   Fibonacci?   Expected")
for val in testList:
    print("  ", val[0], "      ", fb.is_fibonacci(val[0]), "      ", val[1])
    if (val[0] == 63245986):
        print("     (Now exceeds numerical precision)")


####    Tests for Binet's Formula    ####
print ("
Tests for Binet's Formula:")
print("  Number   Fibonacci?   Nearest n   Nearest fib   n range")
for val in testList:
    nrange = fb.n_Binet(val[0])
    print("  ", val[0], "      ", val[1], "      ", round(nrange[0]), "      ", fb.nearest_Binet_fib(val[0]), "      ", nrange)


####    Tests for Saving off Fibonacci Numbers   ###
if not fb.os.path.isfile(fb.filename):
    fb.make_saved_Fibonacci_file()

print ("
Tests for Saving off Fibonacci Numbers:")
saved = [fb.get_nth_saved_Fibonacci_number(n) for n in range(1,11)]
print("  first 10 saved numbers: ", saved)
for n in [12, 20, 40, 80, 98, 99, 100, 101, 200, 1000, 5000]:
    print("   ", n, "th fib: ", fb.get_nth_saved_Fibonacci_number(n))
