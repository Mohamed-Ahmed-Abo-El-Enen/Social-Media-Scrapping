from selenium.common.exceptions import *
from bs4 import BeautifulSoup
import Exceptions
import TimeSteps


def driver_check_exists_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def driver_check_exists_by_id(browser, id):
    try:
        browser.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True


def driver_check_exists_by_tag(browser, tag):
    try:
        browser.find_element_by_tag_name(tag)
    except NoSuchElementException:
        return False
    return True


def driver_click_element(browser, xpath, click_times=0, max_click_times=5):
    try:
        if click_times >= max_click_times:
            return False
        if not driver_check_exists_by_xpath(browser, xpath):
            return False
        browser.find_element_by_xpath(xpath).click()
    except ElementClickInterceptedException:
        TimeSteps.time_between_click()
        driver_click_element(browser, xpath, click_times+1)
    except Exception as e:
        Exceptions.print_exception(e)
    return True


def name_login_button():
    return "login"


def id_login_email_input():
    return "m_login_email"


def id_login_password_input():
    return "m_login_password"


def name_login_password_input():
    return "pass"


def xpath_user_name_ok_button():
    return "//button[@type='submit']"


def name_search_icon_a():
    return "Search"


def id_search_input():
    return "main-search-input"


def xpath_search_result_span(keyword):
    return "//span[contains(text(), '"+keyword+"')]"


def xpath_search_result_div(keyword):
    return "//div[contains(text(), '"+keyword+"')]"


def xpath_publish_a():
    return "//a[@aria-label='Publish']"


def xpath_photo_div():
    return "//button[@title='Add a photo to post']"


def name_description_textarea():
    return "status"


def tag_image_img():
    return "img"


def xpath_post_button():
    return "//button[@value='Post']"


def xpath_back_a():
    return "//a[@data-sigil='back-button']"
