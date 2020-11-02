import sys

from selenium.webdriver.support.wait import WebDriverWait

import TimeSteps
import Utilites as Utl
import GeckoDriver
import Instagram_xpath
import Exceptions as Ex
import CustomTools


class InstagramScraper:
    driver = None

    def __init__(self):

        relative_path = Utl.get_relative_path()

        obj = Utl.read_account_info(relative_path)
        self.instagram_url = obj['INSTAGRAM_URL']['URL']
        self.userName = obj['INSTAGRAM_ACCOUNT_INFO']['USERNAME']
        self.email = obj['INSTAGRAM_ACCOUNT_INFO']['EMAIL']
        self.password = obj['INSTAGRAM_ACCOUNT_INFO']['PASSWORD']
        self.maxFilesPerPost = obj['INSTAGRAM_POST_SETTING']['MAX_FILES_PER_POST']
        self.fileExtension = obj['INSTAGRAM_POST_SETTING']['FILE_EXTENSION']
        self.searchWords = open(relative_path + obj['INSTAGRAM_POST_SETTING']['SEARCH_FILE']).readlines()
        self.replyWords = open(relative_path + obj['INSTAGRAM_POST_SETTING']['REPLY_FILE']).readlines()

        self.posts_resource_directory = Utl.concat_file_to_path(relative_path, "Source Directory")
        self.files = Utl.list_directory_file(self.posts_resource_directory, self.fileExtension)
        self.__remainingFiles = sys.maxsize
        self.__fileIterator = 0
        self.__lastNumFiles = 0

        # self.driver = ChromeDriver.init_chrome_driver()
        self.driver = GeckoDriver.init_gecko_driver()

        self.captionEditText = ""
        self.numTweets = 0

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.driver.close()

    def check_instagram_login(self):
        self.driver.get(self.instagram_url)
        xpath = Instagram_xpath.xpath_login_button()
        TimeSteps.time_between_instruction()
        if Instagram_xpath.driver_check_exists_by_xpath(self.driver, xpath):
            return True
        return False

    def instagram_login(self):
        try:
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_login_button())
            TimeSteps.time_between_click()

            account_login = self.email
            if self.email == "":
                account_login = self.userName
            text_user_name = self.driver.find_element_by_xpath(Instagram_xpath.xpath_username())
            text_user_name.clear()
            text_user_name.send_keys(account_login)

            TimeSteps.time_between_click()

            text_password = self.driver.find_element_by_xpath(Instagram_xpath.xpath_password())
            text_password.clear()
            text_password.send_keys(self.password)
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_login_div())

            TimeSteps.time_after_login()
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_save_not_now())

            TimeSteps.time_between_click()
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_home_screen_cancel())

            TimeSteps.time_between_click()
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_close_notification())

        except Exception as e:
            Ex.print_exception(e)

    def __upload_photo(self):
        try:
            xpath = Instagram_xpath.xpath_new_post_svg()
            Instagram_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_instruction()

            self.__lastNumFiles = min(len(self.files), self.maxFilesPerPost)
            for i in range(self.__fileIterator, self.__fileIterator + self.__lastNumFiles):
                Utl.upload_file(self.files[i])
            self.__fileIterator = self.__fileIterator + self.__lastNumFiles
        except Exception as e:
            Ex.print_exception(e)

    def __click_expand_photo(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_expand_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __add_post_description(self):
        try:
            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_caption_edit_text()
            self.driver.find_element_by_xpath(xpath).send_keys(self.captionEditText)
        except Exception as e:
            Ex.print_exception(e)

    def __add_photo(self):
        try:
            TimeSteps.time_between_instruction()
            self.__lastNumFiles = min(len(self.files), self.maxFilesPerPost)
            for i in range(self.__fileIterator, self.__fileIterator + self.__lastNumFiles):
                tag = "input"
                elements = self.driver.find_elements_by_tag_name(tag)
                elements[3].send_keys(self.files[i])
            self.__fileIterator = self.__fileIterator + self.__lastNumFiles
        except Exception as e:
            Ex.print_exception(e)

    def post(self):
        try:
            xpath = Instagram_xpath.xpath_close_notification()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            self. __upload_photo()
            # self.__add_photo()

            self.__click_expand_photo()

            xpath = Instagram_xpath.xpath_next_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            self.__add_post_description()

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_share_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            self.numTweets = self.numTweets + 1
            TimeSteps.time_between_click()
        except Exception as e:
            Ex.print_exception(e)

    def post_all_files_in_source_folder(self):
        try:
            while self.__remainingFiles != 0:
                self.post()
                self.__remainingFiles = len(self.files) - self.__fileIterator
                TimeSteps.time_between_posts()
                [Utl.move_file(self.files[i]) for i in range(self.__fileIterator - self.__lastNumFiles,
                                                             self.__fileIterator)]
                TimeSteps.time_between_posts()

        except Exception as e:
            Ex.print_exception(e)

    def click_back(self):
        try:
            xpath = Instagram_xpath.xpath_back_svg()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def click_search_explore(self):
        try:
            xpath = Instagram_xpath.xpath_search_explore_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __get_list_accounts(self):
        try:
            xpath = Instagram_xpath.xpath_all_account_search_explore()
            return self.driver.find_elements_by_xpath(xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __click_post_account_follow(self):
        try:
            xpath = Instagram_xpath.xpath_follow_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __get_account_name(self, no_previous):
        try:
            element = self.driver.find_elements_by_tag_name('header')

            xpath = Instagram_xpath.xpath_account_follow_a()
            element = element[1].find_elements_by_xpath(xpath)

            if no_previous:
                account_name = element[1].get_attribute('href')
            else:
                account_name = element[2].get_attribute('href')
            return account_name
        except Exception as e:
            Ex.print_exception(e)

    def post_reply(self, element=None):
        try:
            if element is None:
                element = self.driver

            xpath = Instagram_xpath.xpath_comment()
            Instagram_xpath.driver_click_element(element, xpath)
            reply_edit_text = Utl.get_random_emoji_text(self.replyWords, 3)

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_comment_textarea()
            element.find_element_by_xpath(xpath).send_keys(reply_edit_text)

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_post_button()
            Instagram_xpath.driver_click_element(element, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def click_like(self, element=None):
        try:
            xpath = Instagram_xpath.xpath_like()
            if element is None:
                element = self.driver
            Instagram_xpath.driver_click_element(element, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __like_follow_reply_elements_account(self, followed_accounts, num_follow):
        try:
            len_accounts = sys.maxsize
            account_index = 0
            no_previous = True
            while num_follow > 0 and account_index < len_accounts:
                Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_close_notification())
                accounts = self.__get_list_accounts()
                len_accounts = len(accounts)
                self.driver.execute_script("arguments[0].click();", accounts[account_index])
                TimeSteps.time_between_instruction()
                self.click_like()
                TimeSteps.time_between_instruction()
                self.__click_post_account_follow()
                followed_accounts.append(self.__get_account_name(no_previous))
                no_previous = False
                TimeSteps.time_between_instruction()
                self.post_reply()
                self.click_back()
                TimeSteps.time_between_instruction()
                self.click_back()
                TimeSteps.time_between_click()
                self.click_search_explore()
                num_follow -= 1
                account_index += 1
                TimeSteps.time_between_follow()
            if num_follow > 0:
                self.__like_follow_reply_elements_account(followed_accounts, num_follow)
            return followed_accounts
        except Exception as e:
            Ex.print_exception(e)

    def like_follow_in_search_explore(self, num_follow):
        try:
            self.click_search_explore()
            TimeSteps.time_between_click()
            followed_accounts = []
            self.__like_follow_reply_elements_account(followed_accounts, num_follow)
            return followed_accounts
        except Exception as e:
            Ex.print_exception(e)

    def click_un_follow(self):
        try:
            TimeSteps.time_between_click()
            xpath = Instagram_xpath.xpath_un_follow()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            xpath = Instagram_xpath.xpath_confirm_un_follow()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def un_follow_in_list(self, followed_accounts):
        try:
            for account in followed_accounts:
                TimeSteps.time_between_click()
                self.driver.get(account)
                self.click_un_follow()
                TimeSteps.time_between_un_follow()
        except Exception as e:
            Ex.print_exception(e)

    def post_more_option_click(self, element=None):
        if element is None:
            return
        xpath = Instagram_xpath.xpath_post_more_option_svg()
        Instagram_xpath.driver_click_element(self.driver, xpath)
        xpath = Instagram_xpath.xpath_go_to_post_button()
        Instagram_xpath.driver_click_element(self.driver, xpath)
        TimeSteps.time_between_click()

    def like_reply_on_following_post(self, num_tweets):
        while num_tweets > 0:
            xpath = Instagram_xpath.xpath_post_more_option_svg()
            posts = self.driver.find_elements_by_xpath(xpath)
            if posts is None:
                break
            for post in posts:
                self.post_more_option_click(post)
                self.click_like()
                TimeSteps.time_between_instruction()
                self.post_reply()
                TimeSteps.time_between_instruction()
                self.click_back()
                TimeSteps.time_between_instruction()
                self.click_back()
                num_tweets -= 1
                if num_tweets <= 0:
                    break
                CustomTools.press_end_button(self.driver)
                TimeSteps.time_between_click()

    def __get_instagram_home(self):
        xpath = Instagram_xpath.xpath_profile_svg()
        Instagram_xpath.driver_click_element(self.driver, xpath)

    def __get_all_post_to(self, end_url, list_url):
        TimeSteps.time_between_profile_load()
        xpath = Instagram_xpath.xpath_post_a()
        elements = self.driver.find_elements_by_xpath(xpath)
        profile_post_url = [el.get_attribute('href') for el in elements]
        if end_url in profile_post_url:
            remaining_url = [profile_post_url[index] for index in range(0, profile_post_url.index(end_url))]
            list_url.extend(x for x in remaining_url if x not in list_url)
            return list_url

        list_url.extend(x for x in profile_post_url if x not in list_url)
        CustomTools.press_page_down(self.driver)
        return self.__get_all_post_to(end_url, list_url)

    def get_last_added_to_url(self, end_url):
        list_url = []
        self.__get_instagram_home()
        self.__get_all_post_to(end_url, list_url)
        list_url.reverse()
        print(list_url)
        return list_url
