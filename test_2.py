import logging
from TestPage import ApiTest


def test_step5(good, bad):
    logging.info("Test5 Starting")
    result = ApiTest()
    assert good in result.checkText(bad)


def test_step6(login, text1):
    logging.info("Test6 Starting")
    result = ApiTest()
    assert text1 in result.check_new_post(login)


def test_step7(login, checking_description):
    logging.info("Test7 Starting")
    result = ApiTest()
    result.create_new_post(login)
    assert checking_description in result.get_my_post(login)