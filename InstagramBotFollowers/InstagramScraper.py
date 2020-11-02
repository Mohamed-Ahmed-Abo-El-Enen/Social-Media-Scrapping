import datetime
from selenium.webdriver import ActionChains
import pandas as pd
import TimeSteps
import Utilites as Utl
import Instagram_xpath
import Exceptions as Ex
import ChromeDriver


class InstagramScraper:
    driver = None

    def __init__(self):

        relative_path = Utl.get_relative_path()

        obj = Utl.read_account_info(relative_path)
        self.instagram_url = obj['INSTAGRAM_URL']['URL']
        self.userName = obj['INSTAGRAM_ACCOUNT_INFO']['USERNAME']
        self.email = obj['INSTAGRAM_ACCOUNT_INFO']['EMAIL']
        self.password = obj['INSTAGRAM_ACCOUNT_INFO']['PASSWORD']
        self.following_accounts_file = obj['INSTAGRAM_ACCOUNT_INFO']['FOLLOWING_ACCOUNTS']
        self.driver = ChromeDriver.init_chrome_driver()

        self.search_word = ""
        if not Utl.is_followed_accounts_file_exist(self.following_accounts_file):
            self.following_account_df = pd.DataFrame(columns=["Account_Header", "Date_Time", "Main_Account"])
        else:
            self.following_account_df = Utl.read_followed_accounts_file(self.following_accounts_file)

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

            TimeSteps.time_after_login()
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_home_screen_cancel())

            TimeSteps.time_after_login()
            Instagram_xpath.driver_click_element(self.driver, Instagram_xpath.xpath_close_notification())

        except Exception as e:
            Ex.print_exception(e)

    def click_search_explore(self):
        try:
            xpath = Instagram_xpath.xpath_search_explore_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __set_search_word(self, account_name):
        try:
            xpath = Instagram_xpath.xpath_search_explore_input()
            el = self.driver.find_element_by_xpath(xpath)
            el.send_keys(account_name)
        except Exception as e:
            Ex.print_exception(e)

    def __select_first_search_result(self, account_name):
        try:
            xpath = Instagram_xpath.xpath_search_explore_word(account_name)
            element = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            Ex.print_exception(e)

    def click_account_followers(self, account_name):
        try:
            xpath = Instagram_xpath.xpath_follow_a(account_name)
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __click_account_follow_button(self, element):
        try:
            tag = Instagram_xpath.tag_follower_account_a()
            account_header = element.find_elements_by_tag_name(tag)[-1].text
            if account_header is None:
                return None

            xpath = Instagram_xpath.xpath_follow_button()
            follow_button = element.find_element_by_xpath(xpath)
            actions = ActionChains(self.driver)
            self.driver.execute_script("arguments[0].scrollIntoView();", follow_button)
            actions.click(follow_button).perform()
            self.following_account_df = self.following_account_df.append({"Account_Header": account_header,
                                                                          "Date_Time": datetime.datetime.now(),
                                                                          "Main_Account": self.search_word},
                                                                         ignore_index=True)
        except Exception as e:
            Ex.print_exception(e)

    def __get_accounts_followers(self, num_following, last_index):
        try:
            tag = Instagram_xpath.tag_followers_ul()
            followers_list = self.driver.find_elements_by_tag_name(tag)[-1]
            TimeSteps.time_between_instruction()
            tag = Instagram_xpath.tag_follower_li()
            elements = followers_list.find_elements_by_tag_name(tag)
            TimeSteps.time_between_instruction()
            while last_index < len(elements):

                if last_index >= num_following:
                    return

                self.__click_account_follow_button(elements[last_index])
                last_index += 1
                TimeSteps.time_between_click(20, 30)

            if last_index < num_following:
                self.__get_accounts_followers(num_following, last_index)

        except Exception as e:
            Ex.print_exception(e)

    def refresh_page(self):
        self.driver.refresh()

    def search_for(self, account_name):
        try:
            self.search_word = account_name
            self.click_search_explore()
            TimeSteps.time_between_instruction()
            self.__set_search_word(account_name)
            TimeSteps.time_between_click()
            self.__select_first_search_result(account_name)
            TimeSteps.time_between_instruction()
        except Exception as e:
            Ex.print_exception(e)

    def get_account_followers(self, account_name, num_following=10):
        try:
            self.click_account_followers(account_name)
            TimeSteps.custom_time_between(5, 10)
            self.__get_accounts_followers(num_following, 0)
            TimeSteps.time_between_instruction()
            Utl.save_followed_accounts(self.following_account_df, self.following_accounts_file)

        except Exception as e:
            Ex.print_exception(e)

    def __click_un_follow(self):
        try:
            TimeSteps.time_between_click()
            xpath = Instagram_xpath.xpath_un_follow()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_requested_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_confirm_un_follow()
            Instagram_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def go_account_profile(self, account_name):
        try:
            account_ur = self.instagram_url + '/' + str(account_name) + '/'
            self.driver.get(account_ur)
        except Exception as e:
            Ex.print_exception(e)

    def un_follow_account_file(self):
        try:
            self.following_account_df = Utl.read_followed_accounts_file(self.following_accounts_file)
            self.__un_follow_account()
        except Exception as e:
            Ex.print_exception(e)

    def __un_follow_account(self):
        try:
            for row in self.following_account_df.itertuples():
                self.go_account_profile(row.Account_Header)
                TimeSteps.time_between_click()
                self.__click_un_follow()
                self.following_account_df.drop(row.Index, inplace=True)
                TimeSteps.time_between_un_follow()

            Utl.save_followed_accounts(self.following_account_df, self.following_accounts_file)
        except Exception as e:
            Ex.print_exception(e)

    def reset_followed_last_round(self):
        try:
            self.following_account_df = Utl.read_followed_accounts_file(self.following_accounts_file)
            if not self.following_account_df.empty:
                self.__un_follow_account()
        except Exception as e:
            Ex.print_exception(e)
