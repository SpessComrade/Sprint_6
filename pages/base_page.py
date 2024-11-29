from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def send_keys_to_element(self, locator, text):
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def format_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])