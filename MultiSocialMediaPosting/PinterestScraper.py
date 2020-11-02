import TimeSteps
import Utilites as Utl
import Pinterest_xpath
import Exceptions as Ex


class PinterestScraper:
    def __init__(self, driver):
        relative_path = Utl.get_relative_path()
        obj = Utl.read_account_info(relative_path)
        self.userName = obj['PINTEREST_ACCOUNT_INFO']['USERNAME']
        self.email = obj['PINTEREST_ACCOUNT_INFO']['EMAIL']
        self.password = obj['PINTEREST_ACCOUNT_INFO']['PASSWORD']
        self.driver = driver

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.driver.close()

    def check_pinterest_login(self):
        xpath = Pinterest_xpath.xpath_login_div()
        element = self.driver.find_elements_by_xpath(xpath)
        return element is not None

    def pinterest_login(self):
        try:
            login_url = self.driver.current_url+"login/"
            self.driver.get(login_url)
            TimeSteps.time_between_click()

            id = Pinterest_xpath.xpath_email_id()
            if not Pinterest_xpath.driver_check_exists_by_id(self.driver, id):
                return
            text_email_name = self.driver.find_element_by_id(id)
            text_email_name.send_keys(self.email)
            TimeSteps.time_between_instruction()

            id = Pinterest_xpath.xpath_password_id()
            text_password = self.driver.find_element_by_id(id)
            text_password.send_keys(self.password)

            xpath = Pinterest_xpath.xpath_login_button()
            Pinterest_xpath.driver_click_element(self.driver, xpath)

            TimeSteps.time_after_login()

        except Exception as e:
            Ex.print_exception(e)

    def go_profile(self):
        try:
            xpath = Pinterest_xpath.xpath_profile_img()
            Pinterest_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()
        except Exception as e:
            Ex.print_exception(e)

    def create_pin(self):
        try:
            xpath = Pinterest_xpath.xpath_create_pin_div()
            Pinterest_xpath.driver_click_element(self.driver, xpath)
            TimeSteps.time_between_click()
        except Exception as e:
            Ex.print_exception(e)

    def __click_pin_image(self):
        try:
            tag = Pinterest_xpath.tag_save_pin_image()
            element = self.driver.find_elements_by_tag_name(tag)[1]
            element.click()
        except Exception as e:
            Ex.print_exception(e)

    def __click_add_pin_button(self):
        try:
            xpath = Pinterest_xpath.xpath_add_pin_div()
            Pinterest_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __select_board(self, board_name):
        try:
            xpath = Pinterest_xpath.xpath_select_board_submit_div(board_name)
            Pinterest_xpath.driver_click_element(self.driver, xpath)
        except Exception as e:
            Ex.print_exception(e)

    def __add_pin_title_description(self, description=""):
        try:
            id = Pinterest_xpath.id_add_description_textarea()
            element = self.driver.find_element_by_id(id)
            element.send_keys(description)
        except Exception as e:
            Ex.print_exception(e)

    def __click_on_photo(self, file_path):
        try:
            id = Pinterest_xpath.xpath_photo_input_id()
            element = self.driver.find_element_by_id(id)
            element.send_keys(file_path)
        except Exception as e:
            Ex.print_exception(e)

    def pin(self, file_path, board_name, description=""):
        try:
            self.go_profile()
            TimeSteps.time_between_instruction()
            self.create_pin()
            self.__click_on_photo(file_path)
            TimeSteps.time_between_instruction()
            self.__add_pin_title_description(description)
            TimeSteps.time_between_instruction()
            self.__select_board(board_name)
            TimeSteps.time_between_instruction()
        except Exception as e:
            Ex.print_exception(e)
