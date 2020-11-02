import TimeSteps
import Utilites as Utl
import Facebook_xpath
import Exceptions as Ex


class FacebookScraper:
    def __init__(self, driver, driver_type):
        relative_path = Utl.get_relative_path()
        obj = Utl.read_account_info(relative_path)
        self.userName = obj['FACEBOOK_ACCOUNT_INFO']['USERNAME']
        self.email = obj['FACEBOOK_ACCOUNT_INFO']['EMAIL']
        self.password = obj['FACEBOOK_ACCOUNT_INFO']['PASSWORD']
        self.driver_type = driver_type
        self.driver = driver

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.driver.close()

    def check_facebook_login(self):
        name = Facebook_xpath.name_login_button()
        element = self.driver.find_element_by_name(name)
        return element is not None

    def facebook_login(self):
        try:
            id = Facebook_xpath.id_login_email_input()
            text_email_name = self.driver.find_element_by_id(id)
            text_email_name.send_keys(self.email)
            TimeSteps.time_between_click()

            id = Facebook_xpath.id_login_password_input()
            if Facebook_xpath.driver_check_exists_by_id(self.driver, id):
                text_password = self.driver.find_element_by_id(id)
            else:
                name = Facebook_xpath.name_login_password_input()
                text_password = self.driver.find_element_by_name(name)
            text_password.send_keys(self.password)
            TimeSteps.time_between_click()

            name = Facebook_xpath.name_login_button()
            self.driver.find_element_by_name(name)
            TimeSteps.time_between_click()

            name = Facebook_xpath.name_login_button()
            element = self.driver.find_element_by_name(name)
            element.click()
            TimeSteps.time_between_click()

            xpath = Facebook_xpath.xpath_user_name_ok_button()
            Facebook_xpath.driver_click_element(self.driver, xpath)

        except Exception as e:
            Ex.print_exception(e)

    def go_facebook_page(self, page_name):
        try:
            name = Facebook_xpath.name_search_icon_a()
            search_icon = self.driver.find_element_by_name(name)
            search_icon.click()
            TimeSteps.time_between_click()

            id = Facebook_xpath.id_search_input()
            search_input = self.driver.find_element_by_id(id)
            search_input.send_keys(page_name)
            TimeSteps.time_between_click()

            xpath = Facebook_xpath.xpath_search_result_span(page_name.lower())
            Facebook_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()

            xpath = Facebook_xpath.xpath_search_result_div(page_name)
            Facebook_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()
        except Exception as e:
            Ex.print_exception(e)

    def click_publish_button(self):
        xpath = Facebook_xpath.xpath_publish_a()
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_photo(self, file_path):
        xpath = Facebook_xpath.xpath_photo_div()
        Facebook_xpath.driver_click_element(self.driver, xpath)
        TimeSteps.time_between_instruction()
        if self.driver_type == Utl.DriverType.chrome:
            Utl.chrome_upload_file(file_path)
        else:
            Utl.firefox_upload_file(file_path)

        tag = Facebook_xpath.tag_image_img()
        while not Facebook_xpath.driver_check_exists_by_tag(self.driver, tag):
            TimeSteps.time_between_click()

    def add_description(self, description):
        name = Facebook_xpath.name_description_textarea()
        element = self.driver.find_element_by_name(name)
        element.send_keys(description)

    def click_post_button(self):
        xpath = Facebook_xpath.xpath_post_button()
        elements = self.driver.find_elements_by_xpath(xpath)
        elements[1].click()
        TimeSteps.time_between_instruction()

    def click_back_button(self):
        xpath = Facebook_xpath.xpath_back_a()
        Facebook_xpath.driver_click_element(self.driver, xpath)

    def post(self, file_path, description=""):
        try:
            self.click_publish_button()
            TimeSteps.time_between_click()
            self.click_photo(file_path)
            TimeSteps.time_between_click()
            self.add_description(description)
            TimeSteps.wait_time_between(10, 15)
            self.click_post_button()
            TimeSteps.time_between_click()
            self.click_back_button()

        except Exception as e:
            Ex.print_exception(e)