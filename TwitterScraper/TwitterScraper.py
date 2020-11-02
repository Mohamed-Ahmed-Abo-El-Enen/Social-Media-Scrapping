import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.keys import Keys
import TimeSteps
import Utilites as Utl
import GeckoDriver
import ChromeDriver

import CustomTools
import TwitterXpath as Twitter_xpath
import Exceptions as Ex


class TwitterScraper:
    driver = None

    def __init__(self):

        relative_path = Utl.get_relative_path()

        obj = Utl.read_account_info(relative_path)
        self.twitter_url = obj['TWITTER_URL']['URL']
        self.userName = obj['TWITTER_ACCOUNT_INFO']['USERNAME']
        self.email = obj['TWITTER_ACCOUNT_INFO']['EMAIL']
        self.password = obj['TWITTER_ACCOUNT_INFO']['PASSWORD']
        self.maxFilesPerTweet = obj['TWITTER_TWEET_SETTING']['MAX_FILES_PER_TWEET']
        self.fileExtension = obj['TWITTER_TWEET_SETTING']['FILE_EXTENSION']
        self.searchWords = open(relative_path + obj['TWITTER_TWEET_SETTING']['SEARCH_FILE']).readlines()
        self.replyWords = open(relative_path + obj['TWITTER_TWEET_SETTING']['REPLY_FILE']).readlines()

        self.posts_resource_directory = Utl.concat_file_to_path(relative_path, "Source Directory")
        self.files = Utl.list_directory_file(self.posts_resource_directory, self.fileExtension)
        self.__remainingFiles = sys.maxsize
        self.__fileIterator = 0
        self.__lastNumFiles = 0

        self.driver = GeckoDriver.init_gecko_driver()
        #self.driver = ChromeDriver.init_chrome_driver()
        self.captionEditText = ""
        self.numTweets = 0

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.driver.close()

    def __get_home_tweets(self, xpath):
        tweets = self.driver.find_elements_by_xpath(xpath)
        return tweets

    def __like_tweet(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_like_tweet())
        TimeSteps.time_between_instruction()

    def __unlike_tweet(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_unlike_tweet())
        TimeSteps.time_between_instruction()

    def __re_tweet(self):
        xpath = Twitter_xpath.xpath_retweet()
        if not Twitter_xpath.check_clickable_by_xpath(self.driver, xpath):
            return

        Twitter_xpath.driver_click_element(self.driver, xpath)
        self.__re_tweet_confirm()
        TimeSteps.time_between_instruction()

    def __re_tweet_confirm(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_retweet_confirm())

    def __click_tweet(self, web_element):
        self.driver.execute_script("arguments[0].click();", web_element)

    def __click_tweet_reply(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_reply())

    def __tweet_text_reply(self):
        xpath = Twitter_xpath.xpath_text_reply()
        if not Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath):
            return
        reply_edit_text = Utl.get_random_emoji_text(self.replyWords, 3)
        self.driver.find_element_by_xpath(xpath).send_keys(reply_edit_text)
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_reply_button())

    def __click_tweet_back_button(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_tweet_back_button())

    def __tweet_reply_confirm(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_tweet_confirmation_sheet_confirm())

    def __click_discard_same_reply(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_already_same_reply())

    def __check_user_self_reply(self):
        url_user_name = Utl.get_twitter_user_name(self.driver.current_url)
        if self.userName == url_user_name:
            return True
        return False

    def __close_reply(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_close_reply())

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
            TimeSteps.time_before_login()
            xpath = Twitter_xpath.xpath_login_a()
            Twitter_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()
            account_login = self.email
            if self.email == "":
                account_login = self.userName

            xpath = Twitter_xpath.xpath_username()
            text_user_name = self.driver.find_element_by_xpath(xpath)
            text_user_name.send_keys(account_login)

            TimeSteps.time_between_click()

            xpath = Twitter_xpath.xpath_password()
            text_password = self.driver.find_element_by_xpath(xpath)
            text_password.send_keys(self.password)

            Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_login_div())

            TimeSteps.time_after_login()

        except Exception as e:
            Ex.print_exception(e)

    def check_twitter_login(self):
        self.driver.get(self.twitter_url)
        xpath = Twitter_xpath.xpath_login_a()
        element = self.driver.find_elements_by_xpath(xpath)
        return element is not None

    def go_user_profile(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_user_profile())

    def go_user_home(self):
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_user_home())

    def search_keyword(self):
        try:
            keyword = Utl.get_random_keyword_file(self.searchWords)

            search = self.driver.find_element_by_xpath(Twitter_xpath.xpath_search())
            search.clear()
            search.send_keys(keyword)
            search.send_keys(Keys.ENTER)

        except Exception as e:
            Ex.print_exception(e)

    def follow(self, follow_username):
        self.driver.get(self.twitter_url + '/' + follow_username)
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_follow())

    def un_follow(self, un_follow_username):
        self.driver.get(self.twitter_url + '/' + un_follow_username)
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_un_follow())
        Twitter_xpath.driver_click_element(self.driver, Twitter_xpath.xpath_tweet_confirmation_sheet_confirm())

    def like_num_tweets(self, num_tweets):
        while num_tweets > 0:
            tweets = Twitter_xpath.get_page_tweets(self.driver)
            for i in range(len(tweets)):
                self.__like_tweet()
                num_tweets -= 1
                if num_tweets <= 0:
                    break
                CustomTools.press_page_down(self.driver)

    def like_first_tweets(self):
        tweets = self.__get_home_tweets(Twitter_xpath.xpath_first_tweets())
        for i in range(len(tweets)):
            self.__like_tweet()

    def _auto_alter_appear(self):
        try:
            xpath = Twitter_xpath.xpath_auto_alter_span()
            if not Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath):
                return

            TimeSteps.time_between_alter()
            xpath = Twitter_xpath.xpath_tweet_div_enable()
            Twitter_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_instruction()
            self._auto_alter_appear()
        except Exception as e:
            Ex.print_exception(e)
        return True

    def tweet(self):
        try:
            TimeSteps.time_between_instruction()
            xpath = Twitter_xpath.xpath_tweet_div_disable()
            if self.driver.find_element_by_xpath(xpath) is None:
                self.driver.refresh()
                return False

            TimeSteps.time_between_instruction()
            self.__lastNumFiles = min(len(self.files), self.maxFilesPerTweet)
            for i in range(self.__fileIterator, self.__fileIterator + self.__lastNumFiles):
                self.__upload_file(self.files[i])
            self.__fileIterator = self.__fileIterator + self.__lastNumFiles

            TimeSteps.time_between_click()
            xpath = Twitter_xpath.xpath_caption_edit()
            caption_edit = WebDriverWait(self.driver, 2).until(Ec.element_to_be_clickable((By.XPATH, xpath)))
            caption_edit.send_keys(self.captionEditText)
            self.numTweets = self.numTweets + 1

            TimeSteps.time_between_instruction()
            xpath = Twitter_xpath.xpath_tweet_div_enable()
            Twitter_xpath.driver_click_element(self.driver, xpath)
            self._auto_alter_appear()
            TimeSteps.time_between_click()

        except Exception as e:
            Ex.print_exception(e)
        return True

    def go_home(self):
        try:

            search = self.driver.find_element_by_xpath(Twitter_xpath.xpath_search())

        except Exception as e:
            Ex.print_exception(e)

    def tweets_all_files_in_source_folder(self):
        try:
            self.go_user_home()
            while self.__remainingFiles != 0:
                if not self.tweet():
                    continue
                TimeSteps.time_between_instruction()
                if self.__wait_upload():
                    self.__remainingFiles = len(self.files) - self.__fileIterator
                    [Utl.move_file(self.files[i]) for i in range(self.__fileIterator - self.__lastNumFiles,
                                                                 self.__fileIterator)]
                else:
                    self.driver.refresh()
                TimeSteps.time_between_tweets(120, 300)

        except Exception as e:
            Ex.print_exception(e)

    def tweet_many_tweets(self, num_tweets):
        try:
            while num_tweets > 0:
                self.tweet()
                self.__wait_upload()
                num_tweets -= num_tweets
                TimeSteps.time_between_tweets()

        except Exception as e:
            Ex.print_exception(e)

    def reply_on_tweet(self, num_tweets):

        self.go_user_profile()
        self.userName = Utl.get_twitter_user_name(self.driver.current_url)
        self.go_user_home()

        while num_tweets > 0:
            self.__close_reply()

            tweets = Twitter_xpath.get_page_tweets(self.driver)
            if tweets is None:
                break
            for tweet in tweets:
                xpath = Utl.xpath_soup(tweet)
                if not Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath):
                    continue

                tweet_element = self.driver.find_element_by_xpath(xpath)
                if tweet_element is None:
                    self.__click_tweet_back_button()
                    continue
                if self.__check_user_self_reply():
                    self.__click_tweet_back_button()
                    continue

                self.__click_tweet(tweet_element)
                self.__click_tweet_reply()
                self.__tweet_text_reply()
                self.__tweet_reply_confirm()
                self.__click_discard_same_reply()
                self.__close_reply()
                self.__tweet_reply_confirm()
                self.__click_tweet_back_button()
                num_tweets -= 1
                if num_tweets <= 0:
                    break

            #CustomTools.press_page_down(self.driver)

    def re_tweet_num_tweets(self, num_tweets):
        while num_tweets > 0:
            tweets = Twitter_xpath.get_page_tweets(self.driver)
            for i in range(len(tweets)):
                self.__re_tweet()
                num_tweets -= 1
                if num_tweets <= 0:
                    break
                CustomTools.press_page_down(self.driver)

    def like_reply_re_tweet_on_tweet(self, num_tweets):

        self.go_user_profile()
        self.userName = Utl.get_twitter_user_name(self.driver.current_url)
        self.go_user_home()
        tweets_link = []

        while num_tweets > 0:
            self.__close_reply()

            tweets = Twitter_xpath.get_page_tweets(self.driver)
            if tweets is None:
                break
            for tweet in tweets:
                xpath = Utl.xpath_soup(tweet)
                if not Twitter_xpath.driver_check_exists_by_xpath(self.driver, xpath):
                    CustomTools.press_page_down(self.driver)
                    TimeSteps.time_between_click()
                    continue

                tweet_element = self.driver.find_element_by_xpath(xpath)

                self.__click_tweet(tweet_element)

                if self.driver.current_url in tweets_link:
                    self.__click_tweet_back_button()
                    continue

                if self.__check_user_self_reply():
                    self.__click_tweet_back_button()
                    continue

                tweets_link.append(self.driver.current_url)
                TimeSteps.time_between_instruction()
                self.__like_tweet()
                TimeSteps.time_between_instruction()
                self.__re_tweet()
                TimeSteps.time_between_instruction()
                self.__click_tweet_reply()
                TimeSteps.time_between_instruction()
                self.__tweet_text_reply()
                self.__tweet_reply_confirm()
                self.__click_discard_same_reply()
                TimeSteps.time_between_instruction()
                self.__close_reply()
                self.__tweet_reply_confirm()
                TimeSteps.time_between_instruction()
                self.__click_tweet_back_button()
                #TimeSteps.time_between_tweets()
                num_tweets -= 1
                if num_tweets <= 0:
                    break
