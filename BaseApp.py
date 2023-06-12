import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.address = "https://test-stand.gb.ru"
        self.driver = driver
    def start_browser(self):
        self.driver.get(self.address)

    def find_element(self, locator, time=3):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return (element.value_of_css_property(property))
        logging.error(f"Property {property} not found in element with locator {locator}")

    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.address)
        except:
            logging.exception("Exception while open site")
            start_browser = None
        return start_browser
    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None



