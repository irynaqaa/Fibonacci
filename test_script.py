import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

####    Tests for Audible Artifacts    ####
print("Testing for Audible Artifacts...")

# Test 1: Verify no audible artifacts during frequency sweep
driver = webdriver.Chrome()
driver.get("http://localhost:5000/audio_analysis")  # Adjust URL as necessary
start_signal_button = driver.find_element(By.ID, "start_signal_button")
start_signal_button.click()
time.sleep(1)  # Wait for the signal to start
# Conduct frequency sweep from 20 Hz to 20,000 Hz
sweep_button = driver.find_element(By.ID, "frequency_sweep_button")
sweep_button.click()
time.sleep(5)  # Wait for the sweep to complete
# Analyze the output spectrum for artifacts
output_spectrum = driver.find_element(By.ID, "output_spectrum")
assert "No artifacts detected" in output_spectrum.text

# Test 2: Measure frequency response after applying the feature
apply_feature_button = driver.find_element(By.ID, "apply_feature_button")
apply_feature_button.click()
time.sleep(1)  # Wait for the feature to apply
sweep_button.click()  # Conduct another frequency sweep
time.sleep(5)  # Wait for the sweep to complete
assert "No artifacts detected" in output_spectrum.text
driver.quit()

####    Tests for Fibonacci Numbers    ####
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
