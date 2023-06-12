from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml, requests
from zeep import Client, Settings

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
user = testdata["user"]
passwd = testdata["passwd"]
title = testdata["title"]
description = testdata["description"]
content = testdata["content"]
class TestLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
class Operations(BasePage, TestLocators):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name  = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text


# ENTER TEXT

    def enter_login(self, word):
        self.enter_text_into_field(TestLocators.ids["x_selector_1"], word, description="Login format")
    def enter_passwd(self, word):
        self.enter_text_into_field(TestLocators.ids["x_selector_2"], word, description="Password format")
    def input_title(self, word):
        self.enter_text_into_field(TestLocators.ids["title_selector"], word, description="Title format")
    def input_description(self, word):
        self.enter_text_into_field(TestLocators.ids["description_selector"], word, description="Description format")
    def input_content(self, word):
        self.enter_text_into_field(TestLocators.ids["content_selector"], word, description="Content format")
    def enter_name(self, word):
        self.enter_text_into_field(TestLocators.ids["field_name"], word, description="Name format")
    def enter_email(self, word):
        self.enter_text_into_field(TestLocators.ids["field_email"], word, description="Email format")
    def enter_message(self, word):
        self.enter_text_into_field(TestLocators.ids["field_message"], word, description="Message format")

# CLICK
    def click_login_btn(self):
        self.click_button(TestLocators.ids["btn_selector"], description="login")
    def click_create_btn(self):
        self.click_button(TestLocators.ids["create_btn"], description="Create")
    def click_btn_save(self):
        self.click_button(TestLocators.ids["btn_save"], description="Save")
    def click_contact_us(self):
        self.click_button(TestLocators.ids["btn_contact_us"], description="Contact us")
    def save_contact_us(self):
        self.click_button(TestLocators.ids["btn_save_contact_us"], description="Save contact us")

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestLocators.ids["x_selector_3"], description="error")
    def find_hello_user(self):
        return self.get_text_from_element(TestLocators.ids["hello_user"], description="error")
    def result_title(self):
        return self.get_text_from_element(TestLocators.ids["result_title"], description="username")
    def check_alert(self):
        try:
            alert = self.driver.switch_to.alert
            logging.info(f'Error {alert.text}')
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None


class ApiTest:

    def check_new_post(self, token):
        try:
            new_post = requests.get("https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token},
                                    params={'owner': 'notMe'})
            listdescr = [i["description"] for i in new_post.json()["data"]]
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We find text {listdescr} in field {new_post.json()}")
        return listdescr

    def create_new_post(self, token):
        with open("testdata.yaml") as f:
            user = yaml.safe_load(f)
        try:
            response = requests.post("https://test-stand.gb.ru/api/posts", headers={'X-Auth-Token': token},
                                     data={'title': user['title'],
                                           'description': user['description'],
                                           'content': user['content']})
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We are creating a new post {response.json()}")
        return response.json()

    def get_my_post(self, token):
        try:
            response = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
            listdescr = [i['description'] for i in response.json()['data']]
        except:
            logging.exception(f"Exception while get test from {token}")
            return None
        logging.debug(f"We getting description new post {listdescr}")
        return listdescr

    def checkText(self, word):
        with open('testdata.yaml') as f:
            wsdl = yaml.safe_load(f)['wsdl']

        settings = Settings(strict=False)
        client = Client(wsdl=wsdl, settings=settings)

        try:
            response = client.service.checkText(word)[0]['s']
        except:
            logging.exception("Find element exception")
            response = None
        return response



