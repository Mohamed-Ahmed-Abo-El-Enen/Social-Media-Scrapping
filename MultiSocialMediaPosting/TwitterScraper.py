from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import TimeSteps
import Utilites as Utl
import TwitterXpath as Twitter_xpath
import Exceptions as Ex


class TwitterScraper:
    def __init__(self, driver):
        relative_path = Utl.get_relative_path()
        obj = Utl.read_account_info(relative_path)
        self.userName = obj['TWITTER_ACCOUNT_INFO']['USERNAME']
        self.email = obj['TWITTER_ACCOUNT_INFO']['EMAIL']
        self.password = obj['TWITTER_ACCOUNT_INFO']['PASSWORD']
        self.driver = driver

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.driver.close()

    def __get_home_tweets(self, xpath):
        tweets = self.driver.find_elements_by_xpath(xpath)
        return tweets

    def __upload_file(self, file_path):
        try:
            xpath = Twitter_xpath.xpath_upload_file_button()
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(file_path)
            TimeSteps.time_between_instruction()

        except Exception as e:
            Ex.print_exception(e)

    def __wait_upload(self):
        xpath = Twitter_xpath.xpath_tweet_div_disable()
        Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath)
        is_tweet_button = Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath)
        xpath = Twitter_xpath.xpath_caption_edit()
        is_caption_edit = Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath)

        if is_tweet_button and is_caption_edit:
            return True
        TimeSteps.upload_wait_time()
        return self.__wait_upload()

    def twitter_login(self):
        try:
            account_login = self.email
            if self.email == "":
                account_login = self.userName

            xpath = Twitter_xpath.xpath_username()
            text_user_name = self.driver.find_element_by_xpath(xpath)
            text_user_name.send_keys(account_login)

            TimeSteps.time_between_instruction()

            xpath = Twitter_xpath.xpath_password()
            text_password = self.driver.find_element_by_xpath(xpath)
            text_password.send_keys(self.password)

            xpath = Twitter_xpath.xpath_login_div()
            Twitter_xpath.driver_click_element(self.driver, xpath)

            TimeSteps.time_after_login()
            self.go_user_home()
        except Exception as e:
            Ex.print_exception(e)

    def check_twitter_login(self):
        xpath = Twitter_xpath.xpath_login_a()
        TimeSteps.time_between_instruction()
        if Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath):
            return True
        return False

    def go_user_home(self):
        try:
            xpath = Twitter_xpath.xpath_user_home()
            Twitter_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def tweet(self, file_path, description):
        try:
            xpath = Twitter_xpath.xpath_tweet_div_disable()
            if self.driver.find_element_by_xpath(xpath) is None:
                self.driver.refresh()
                return False

            self.__upload_file(file_path)

            xpath = Twitter_xpath.xpath_caption_edit()
            caption_edit = WebDriverWait(self.driver, 2).until(Ec.element_to_be_clickable((By.XPATH, xpath)))
            caption_edit.send_keys(description)

            xpath = Twitter_xpath.xpath_tweet_div_enable()
            Twitter_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()

        except Exception as e:
            Ex.print_exception(e)
        return True



