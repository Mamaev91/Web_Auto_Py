import pytest

@pytest.fixture()
def x_selector_1():
    return "/html/body/div/main/div/div/div/form/div[1]/label/input"
@pytest.fixture()
def x_selector_2():
    return "/html/body/div/main/div/div/div/form/div[2]/label/input"
@pytest.fixture()
def x_selector_3():
    return '//*[@id="app"]/main/div/div/div[2]/h2'
@pytest.fixture()
def btn_selector():
    return "button"
@pytest.fixture()
def result():
    return "401"
@pytest.fixture()
def hello_user():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'
@pytest.fixture()
def create_btn():
    return '//*[@id="create-btn"]'
@pytest.fixture()
def title_selector():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'
@pytest.fixture()
def description_selector():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
@pytest.fixture()
def content_selector():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
@pytest.fixture()
def btn_save():
    return '//*[@id="create-item"]/div/div/div[7]/div/button'
@pytest.fixture()
def result_title():
    return '//*[@id="app"]/main/div/div[1]/h1'


