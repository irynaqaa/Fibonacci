from .base import BasePage

class FibonacciPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://localhost:5000")