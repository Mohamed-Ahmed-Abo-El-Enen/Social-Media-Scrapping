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
            return driver_click_element(browser, xpath, click_times + 1, max_click_times)
        browser.find_element_by_xpath(xpath).click()
    except ElementClickInterceptedException:
        return driver_click_element(browser, xpath, click_times + 1, max_click_times)
    except NoSuchElementException:
        return driver_click_element(browser, xpath, click_times + 1, max_click_times)
    except Exception as e:
        Exceptions.print_exception(e)


def check_clickable_by_xpath(element, xpath):
    try:
        element.find_element_by_xpath(xpath)
    except ElementClickInterceptedException:
        return False
    return True


def xpath_username():
    return "//input[@name='session[username_or_email]']"


def xpath_password():
    return "//input[@name='session[password]']"


def xpath_login_div():
    return "//div[@data-testid='LoginForm_Login_Button']"


def xpath_login_a():
    return "//a[@data-testid='loginButton' or @href='/login']"


def xpath_caption_edit():
    return "//div[@data-testid='tweetTextarea_0']"


def xpath_tweet_div_enable():
    return "//div[@data-testid='tweetButtonInline']"


def xpath_tweet_div_disable():
    return "//div[@data-testid='tweetButtonInline' and @aria-disabled='true']"


def xpath_upload_file_button():
    return "//input[@type='file']"


def xpath_wait_new_page_progress_bar():
    return '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[4]' \
           '/div/div/section/div/div/div/div[4]/div/div/div'


def xpath_user_profile():
    return "//a[@aria-label='Profile']"


def xpath_user_home():
    return "//a[@data-testid='AppTabBar_Home_Link']"
