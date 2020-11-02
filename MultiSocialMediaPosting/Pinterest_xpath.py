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


def xpath_login_div():
    return "//div[text()='Continue with email']"


def xpath_email_id():
    return "email"


def xpath_password_id():
    return "password"


def xpath_login_button():
    return "//button[@type='submit']"


def xpath_profile_img():
    return "//img[@alt='My profile']"


def xpath_create_pin_div():
    return "//div[@data-test-id='createMenuCreateButton']"


def xpath_submit_link_div():
    return "//div[@data-test-id='website-link-submit-button']"


def xpath_save_from_site_div():
    return "//div[@data-test-id='save-from-site-button']"


def id_site_url_input():
    return "pin-draft-website-link"


def xpath_board_dropdown_button():
    return "//button[@data-test-id='board-dropdown-select-button']"


def tag_save_pin_image():
    return "img"


def xpath_add_pin_div():
    return "//div[@data-test-id='scrape-view-add-button']"


def xpath_search_board_input():
    return "//input[@aria-label='Search through your boards']"


def xpath_select_board_submit_div(board_name):
    return "//div[contains(text(), '"+board_name+"')]"


def id_add_description_textarea():
    return "description"


def xpath_save_button():
    return "//button[@data-test-id='board-dropdown-save-button']"


def xpath_close_button():
    return "//button[@aria-label='close']"


def xpath_photo_input_id():
    return "upload-pin"
