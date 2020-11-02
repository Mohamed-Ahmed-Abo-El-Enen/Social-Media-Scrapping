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


def xpath_upload_file_button():
    return "//input[@type='file']"


def xpath_new_post_svg():
    return "//*[local-name()='svg'][@aria-label='New Post']"


def xpath_expand_button():
    return "//span[text()='Expand']"


def xpath_next_button():
    return "//button[text()='Next']"


def xpath_caption_edit_text():
    return "//textarea[@aria-label='Write a caption…']"


def xpath_share_button():
    return "//button[text()='Share']"


def xpath_search_explore_button():
    return "//a[@href='/explore/']"


def xpath_all_account_search_explore():
    return "//a[@href]"


def xpath_follow_button():
    return "//button[text()='Follow']"


def xpath_like():
    return "//*[local-name()='svg'][@aria-label='Like']"


def xpath_un_follow():
    return "//span[@aria-label='Following']"


def xpath_confirm_un_follow():
    return "//button[text()='Unfollow']"


def xpath_comment():
    return "//*[local-name()='svg'][@aria-label='Comment']"


def xpath_comment_textarea():
    return "//textarea[@aria-label]"


def xpath_post_button():
    return "//button[text()='Post']"


def xpath_back_svg():
    return "//*[local-name()='svg'][@aria-label='Back']"


def xpath_account_follow_header():
    return "//a[text()]"


def xpath_account_follow_a():
    return "//a[text()]"


def xpath_post_more_option_svg():
    return "//*[local-name()='svg'][@aria-label='More options']"


def xpath_go_to_post_button():
    return "//button[text()='Go to post']"


def xpath_profile_svg():
    return "//*[local-name()='svg'][@aria-label='Profile']"


def xpath_post_a():
    return "//a[contains(@href, '/p/')]"
