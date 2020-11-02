from selenium.common.exceptions import *

import Exceptions
import TimeSteps


def driver_check_exists_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def driver_click_element(browser, xpath, click_times=0, max_click_times=5):
    try:
        if click_times >= max_click_times:
            return
        element = browser.find_element_by_xpath(xpath)
        if element is None:
            TimeSteps.time_between_instruction()
            return driver_click_element(browser, xpath, click_times+1, max_click_times)
        browser.find_element_by_xpath(xpath).click()
    except ElementClickInterceptedException:
        return driver_click_element(browser, xpath, click_times+1, max_click_times)
    except NoSuchElementException:
        return driver_click_element(browser, xpath, click_times+1, max_click_times)
    except Exception as e:
        Exceptions.print_exception(e)


def check_clickable_by_xpath(element, xpath):
    try:
        element.find_element_by_xpath(xpath)
    except ElementClickInterceptedException:
        return False
    return True


def xpath_username():
    return "//input[@aria-label='Phone number, username, or email']"


def xpath_password():
    return "//input[@aria-label='Password']"


def xpath_login_button():
    return "//button[text()='Log In']"


def xpath_login_div():
    return "//div[text()='Log In']"


def xpath_save_not_now():
    return "//button[text()='Not Now']"


def xpath_home_screen_cancel():
    return "//button[text()='Cancel']"


def xpath_close_notification():
    return "//button[text()='Not Now']"


def xpath_search_explore_button():
    return "//a[@href='/explore/']"


def xpath_search_explore_input():
    return "//input[@type='search']"


def xpath_search_explore_word(search_word):
    return '//a[@href="/'+search_word+'/"]'


def xpath_follow_a(search_word):
    return '//a[@href="/'+search_word+'/followers/"]'


def tag_followers_ul():
    return "ul"


def tag_follower_li():
    return "li"


def tag_follower_account_a():
    return "a"


def xpath_follow_button():
    return "//button[text()='Follow']"


def xpath_un_follow():
    return "//span[@aria-label='Following']"


def xpath_requested_button():
    return "//button[text()='Requested']"


def xpath_confirm_un_follow():
    return "//button[text()='Unfollow']"


