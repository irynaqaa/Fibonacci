import pytest
from pages.fibonacci_page import FibonacciPage

def test_fibonacci_number_one):
    driver = webdriver.Chrome()
    fibonacci_page = FibonacciPage(driver)
    fibonacci_page.driver.find_element_by_name("number").send_keys("1")
    fibonacci_page.driver.find_element_by_name("calculate").click()
    result = fibonacci_page.driver.find_element_by_name("result").text
    assert result == "1"