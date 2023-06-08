from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
user = testdata["user"]
passwd = testdata["passwd"]
title = testdata["title"]
description = testdata["description"]
content = testdata["content"]
class TestLocators:
    x_selector_1 = (By.XPATH, "/html/body/div/main/div/div/div/form/div[1]/label/input")

    x_selector_2 = (By.XPATH, "/html/body/div/main/div/div/div/form/div[2]/label/input")

    x_selector_3 = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')

    btn_selector = (By.CSS_SELECTOR, "button")

    hello_user = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')

    create_btn = (By.CSS_SELECTOR, "button")

    title_selector = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')

    description_selector = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')

    content_selector = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')

    btn_save = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')

    result_title = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')




    btn_contact_us = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")

    field_name = (By.XPATH, """//*[@id="contact"]/div[1]/label""")

    field_email = (By.XPATH, """//*[@id="contact"]/div[2]/label""")

    field_message = (By.XPATH, """//*[@id="contact"]/div[3]/label""")

    btn_save_contact_us = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class Operations(BasePage, TestLocators):
    def enter_login(self):
        logging.info("Enter login")
        input1 = self.find_element(self.x_selector_1)
        input1.send_keys("test")
    def enter_passwd(self):
        logging.info("Enter password")
        input2 = self.find_element(self.x_selector_2)
        input2.send_keys("test")
    def click_login_btn(self):
        logging.info("Click button")
        btn = self.find_element(self.btn_selector)
        btn.click()
    def get_error_text(self):
        err_label = self.find_element(self.x_selector_3)
        err_text = err_label.text
        logging.info(f"Error {err_text}")
        return err_text
    def enter_login_value(self):
        logging.info("Enter login")
        input1 = self.find_element(self.x_selector_1)
        input1.clear()
        input1.send_keys(user)
    def enter_passwd_value(self):
        logging.info("Enter password")
        input2 = self.find_element(self.x_selector_2)
        input2.clear()
        input2.send_keys(passwd)

    def find_hello_user(self):
        find_element = self.find_element(self.hello_user)
        element = find_element.text
        return element

    def click_create_btn(self):
        logging.info("Click create button")
        c_btn = self.find_element(self.create_btn)
        c_btn.click()

    def input_title(self):
        input_title = self.find_element(self.title_selector)
        input_title.clear()
        input_title.send_keys(title)
    def input_description(self):
        input_description = self.find_element(self.description_selector)
        input_description.clear()
        input_description.send_keys(description)
    def input_content(self):
        input_content = self.find_element(self.content_selector)
        input_content.clear()
        input_content.send_keys(content)
    def click_btn_save(self):
        logging.info("Click save button")
        s_btn = self.find_element(self.btn_save)
        s_btn.click()
    def result_title(self):
        result_title = self.find_element(self.result_title)
        logging.info(f'Error {result_title.text}')
        return result_title.text

    def click_contact_us(self):
        logging.info('Click button contact us')
        btn_contact = self.find_element(self.btn_contact_us)
        btn_contact.click()

    def enter_name(self, word):
        logging.info('Enter name ')
        input_name = self.find_element(self.field_name)
        input_name.send_keys(word)

    def enter_email(self, word):
        logging.info('Enter email')
        input_email = self.find_element(self.field_email)
        input_email.send_keys(word)

    def enter_message(self, text):
        logging.info('Enter message')
        input_message = self.find_element(self.field_message)
        input_message.send_keys(text)

    def save_contact_us(self):
        logging.info('Click button save message')
        btn_save_c_u = self.find_element(self.btn_save_contact_us)
        btn_save_c_u.click()

    def check_alert(self):
        alert = self.driver.switch_to.alert
        logging.info(f'Error {alert.text}')
        return alert.text





