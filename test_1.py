import yaml
from BaseApp import BasePage
import time
from TestPage import Operations

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
user = testdata["user"]
passwd = testdata["passwd"]
title = testdata["title"]
description = testdata["description"]
content = testdata["content"]
name = testdata["name"]
email = testdata["email"]
message = testdata["message"]


def test_step1(ExpErr1, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login("test")
    page.enter_passwd("test")
    page.click_login_btn()
    assert page.get_error_text() == ExpErr1

def test_step2(ExpErr2, browser):
    page = Operations(browser)
    page.enter_login(user)
    page.enter_passwd(passwd)
    page.click_login_btn()
    assert page.find_hello_user() == ExpErr2
#

def test_step3(browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login(user)
    page.enter_passwd(passwd)
    page.click_login_btn()
    page.click_create_btn()
    page.input_title(title)
    page.input_description(description)
    page.input_content(content)
    page.click_btn_save()
    time.sleep(2)
    assert page.result_title() == testdata["title"]

def test_step4(browser, ExpErr3):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.click_contact_us()
    page.enter_name(name)
    page.enter_email(email)
    page.enter_message(message)
    time.sleep(2)
    page.save_contact_us()
    time.sleep(2)
    assert page.check_alert() == ExpErr3


    # css_selector = "span.mdc-text-field__ripple"
    # print(site.get_element_property("css", css_selector, "height"))
    #
    # xpath = '//*[@id="login"]/div[3]/button/div'
    # print(site.get_element_property("xpath", xpath, "color"))