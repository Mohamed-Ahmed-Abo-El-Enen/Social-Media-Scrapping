import TimeSteps
import Utilites as Utl
import Instagram_xpath
import Exceptions as Ex


class InstagramScraper:
    def __init__(self, driver, driver_type):
        relative_path = Utl.get_relative_path()
        obj = Utl.read_account_info(relative_path)
        self.userName = obj['INSTAGRAM_ACCOUNT_INFO']['USERNAME']
        self.email = obj['INSTAGRAM_ACCOUNT_INFO']['EMAIL']
        self.password = obj['INSTAGRAM_ACCOUNT_INFO']['PASSWORD']
        self.driver_type = driver_type
        self.driver = driver

    def check_instagram_login(self):
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

    def __upload_photo(self, file_path):
        try:
            xpath = Instagram_xpath.xpath_new_post_svg()
            Instagram_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_instruction()
            if self.driver_type == Utl.DriverType.chrome:
                Utl.chrome_upload_file(file_path)
            else:
                Utl.firefox_upload_file(file_path)

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

    def __add_post_description(self, description):
        try:
            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_caption_edit_text()
            self.driver.find_element_by_xpath(xpath).send_keys(description)
        except Exception as e:
            Ex.print_exception(e)

    def share(self, file_path, description):
        try:
            xpath = Instagram_xpath.xpath_close_notification()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            self. __upload_photo(file_path)

            self.__click_expand_photo()

            xpath = Instagram_xpath.xpath_next_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            self.__add_post_description(description)

            TimeSteps.time_between_instruction()
            xpath = Instagram_xpath.xpath_share_button()
            Instagram_xpath.driver_click_element(self.driver, xpath)

            TimeSteps.time_between_click()
        except Exception as e:
            Ex.print_exception(e)
