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


def get_page_tweets(browser):
    soup = BeautifulSoup(browser.page_source, 'lxml')
    return soup.find_all('div', {'data-testid': 'tweet'})


def xpath_username():
    return "//input[@name='session[username_or_email]']"


def xpath_password():
    return "//input[@name='session[password]']"


def xpath_login_div():
    return "//div[@data-testid='LoginForm_Login_Button']"


def xpath_login_a():
    return "//a[@data-testid='loginButton' or @href='/login']"


def xpath_search():
    return "//input[@data-testid='SearchBox_Search_Input']"


def xpath_first_tweets():
    return "//div[@data-testid='tweet']"


def xpath_time_line_tweet():
    return "//div[@aria-label='Timeline: Your Home Timeline']"


def xpath_like_tweet():
    return "//div[@data-testid='like']"


def xpath_unlike_tweet():
    return "//div[@data-testid='unlike']"


def xpath_retweet():
    return "//div[@data-testid='retweet']"


def xpath_retweet_confirm():
    return "//div[@data-testid='retweetConfirm']"


def xpath_reply():
    return "//div[@data-testid='reply']"


def xpath_text_reply():
    return "//div[@data-testid='tweetTextarea_0']"


def xpath_reply_button():
    return "//div[@data-testid='tweetButton']"


def xpath_follow():
    return "//span[text()='Follow']"


def xpath_already_same_reply():
    return "//span[text()='Whoops! You already said that.']"


def xpath_un_follow():
    return "//span[text()='Following']"


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


def xpath_tweet_back_button():
    return "//div[@aria-label='Back']"


def xpath_tweet_confirmation_sheet_confirm():
    return "//div[@data-testid='confirmationSheetConfirm']"


def xpath_user_reply(user_name):
    return "//div[@href='"+user_name+"']"


def xpath_close_reply():
    return "//div[@aria-label='Close']"


def xpath_user_profile():
    return "//a[@aria-label='Profile']"


def xpath_user_home():
    return "//a[@data-testid='AppTabBar_Home_Link']"


def xpath_auto_alter_span():
    return "//span[text()='Something went wrong, but don’t fret — let’s give it another shot.']"