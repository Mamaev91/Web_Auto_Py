import yaml
from module import Site
import pytest
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
user = testdata["user"]
passwd = testdata["passwd"]
site = Site(testdata["address"])
title = testdata["title"]
description = testdata["description"]
content = testdata["content"]

# def test_step1(x_selector_1, x_selector_2, x_selector_3, btn_selector, result):
#     input1 = site.find_element("xpath", x_selector_1)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", x_selector_2)
#     input2.send_keys("test")
#     btn_selector = btn_selector
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     err_label = site.find_element("xpath", x_selector_3)
#     assert err_label.text == result
#     # site.close()

# def test_step2(x_selector_1, x_selector_2, btn_selector, hello_user):
#     input1 = site.find_element("xpath", x_selector_1)
#     input1.clear()
#     input1.send_keys(user)
#     input2 = site.find_element("xpath", x_selector_2)
#     input2.clear()
#     input2.send_keys(passwd)
#     btn_selector = btn_selector
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     element = site.find_element("xpath", hello_user)
#     assert element.text == f"Hello, {user}"

    # site.close()

def test_step3(x_selector_1, x_selector_2, btn_selector, create_btn, title_selector, description_selector,
               content_selector, btn_save, result_title):
    input1 = site.find_element("xpath", x_selector_1)
    input1.clear()
    input1.send_keys(user)
    input2 = site.find_element("xpath", x_selector_2)
    input2.clear()
    input2.send_keys(passwd)
    btn_selector = btn_selector
    btn = site.find_element("css", btn_selector)
    btn.click()
    btn_create = create_btn
    c_btn = site.find_element("xpath", btn_create)
    c_btn.click()
    time.sleep(3)
    input_title = site.find_element("xpath", title_selector)
    input_title.clear()
    input_title.send_keys(title)
    input_description = site.find_element("xpath", description_selector)
    input_description.clear()
    input_description.send_keys(description)
    input_content = site.find_element("xpath", content_selector)
    input_content.clear()
    input_content.send_keys(content)
    time.sleep(5)
    btn_save = btn_save
    s_btn = site.find_element("xpath", btn_save)
    time.sleep(3)
    s_btn.click()
    time.sleep(3)
    result_title = site.find_element("xpath", result_title)
    assert result_title.text == title
    site.close()




    # css_selector = "span.mdc-text-field__ripple"
    # print(site.get_element_property("css", css_selector, "height"))
    #
    # xpath = '//*[@id="login"]/div[3]/button/div'
    # print(site.get_element_property("xpath", xpath, "color"))