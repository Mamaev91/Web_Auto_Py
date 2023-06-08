import yaml
from BaseApp import BasePage
import time
from TestPage import Operations

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# user = testdata["user"]
# passwd = testdata["passwd"]
# title = testdata["title"]
# description = testdata["description"]
# content = testdata["content"]

def test_step1(ExpErr1, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login()
    page.enter_passwd()
    page.click_login_btn()
    assert page.get_error_text() == ExpErr1

def test_step2(ExpErr2, browser):
    site = BasePage(browser)
    page = Operations(browser)
    page.enter_login_value()
    page.enter_passwd_value()
    page.click_login_btn()
    assert page.find_hello_user() == ExpErr2
#

def test_step3(browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login_value()
    page.enter_passwd_value()
    page.click_login_btn()
    page.click_create_btn()
    page.input_title()
    page.input_description()
    page.input_content()
    page.click_btn_save()
    time.sleep(2)
    assert page.result_title() == testdata["title"]

def test_step4(browser, ExpErr3):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.click_contact_us()
    page.enter_name(testdata["name"])
    page.enter_email(testdata["email"])
    page.enter_message(testdata["message"])
    page.save_contact_us()
    time.sleep(2)
    assert page.check_alert() == ExpErr3


    # css_selector = "span.mdc-text-field__ripple"
    # print(site.get_element_property("css", css_selector, "height"))
    #
    # xpath = '//*[@id="login"]/div[3]/button/div'
    # print(site.get_element_property("xpath", xpath, "color"))