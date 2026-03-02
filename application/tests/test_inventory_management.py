import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    raise ImportError("Ensure that the 'webdriver_manager' package is installed and accessible in your environment.")

@pytest.fixture(scope="module")
def setup_module():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def test_add_product(setup_module):
    driver = setup_module
    driver.get("http://localhost:3000/add-product")  # Adjust URL as needed
    driver.find_element(By.NAME, "name").send_keys("Test Product")
    driver.find_element(By.NAME, "price").send_keys("10.99")
    driver.find_element(By.NAME, "description").send_keys("A test product.")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)  # Wait for the page to update
    assert "Test Product" in driver.page_source

def test_edit_product(setup_module):
    driver = setup_module
    driver.get("http://localhost:3000/products")  # Adjust URL as needed
    driver.find_element(By.XPATH, "//tr[td[text()='Test Product']]/td/a[text()='Edit']").click()
    driver.find_element(By.NAME, "price").clear()
    driver.find_element(By.NAME, "price").send_keys("12.99")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)  # Wait for the page to update
    assert "12.99" in driver.page_source

def test_remove_product(setup_module):
    driver = setup_module
    driver.get("http://localhost:3000/products")  # Adjust URL as needed
    driver.find_element(By.XPATH, "//tr[td[text()='Test Product']]/td/a[text()='Remove']").click()
    driver.find_element(By.ID, "confirm").click()  # Confirm removal
    time.sleep(2)  # Wait for the page to update
    assert "Test Product" not in driver.page_source

def test_perform_inventory_operations(setup_module):
    driver = setup_module
    driver.get("http://localhost:3000/inventory")  # Adjust URL as needed
    driver.find_element(By.NAME, "product_id").send_keys("1")  # Assuming product ID 1
    driver.find_element(By.NAME, "operation_type").send_keys("add")
    driver.find_element(By.NAME, "number_of_products").send_keys("5")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)  # Wait for the page to update
    assert "5" in driver.page_source

def test_view_inventory(setup_module):
    driver = setup_module
    driver.get("http://localhost:3000/inventory")  # Adjust URL as needed
    assert "Test Product" in driver.page_source
    assert "5" in driver.page_source  # Assuming the inventory count is 5