import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
user = testdata["user"]

@pytest.fixture()
def ExpErr1():
    return "401"
@pytest.fixture()
def ExpErr2():
    return "Hello, {}".format(user)
@pytest.fixture()
def ExpErr3():
    return "Form successfully submitted"

@pytest.fixture(scope="session")
def browser():
    # if browser == "firefox":
    # service = Service(executable_path=GeckoDriverManager().install())
    # options = webdriver.FirefoxOptions()
    # driver = webdriver.Firefox(service=service, options=options)
    # elif browser == "chrome":
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

