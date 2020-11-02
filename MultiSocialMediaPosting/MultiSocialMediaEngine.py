import GeckoDriver
import ChromeDriver
import TimeSteps
import sys
import Utilites as Utl
import InstagramScraper as instScraper
import PinterestScraper as pinScraper
import FacebookScraper as facScraper
import TwitterScraper as twtScraper
import Exceptions as Ex


class MultiSocialMediaEngine:
    def __init__(self, pages_url, driver_type=Utl.DriverType.chrome):
        self.pages_url = pages_url
        self.multi_tab_dic = dict()

        self.driver_type = driver_type
        if self.driver_type == Utl.DriverType.chrome:
            self.browser = ChromeDriver.init_chrome_driver()
        else:
            self.browser = GeckoDriver.init_gecko_driver()
        self.open_multi_tabs()
        relative_path = Utl.get_relative_path()
        self.fileExtension = ".jpg"
        self.posts_resource_directory = Utl.concat_file_to_path(relative_path, "Source Directory")
        self.files = Utl.list_directory_file(self.posts_resource_directory, self.fileExtension)
        self.__remainingFiles = sys.maxsize
        self.__fileIterator = 0
        self.__lastNumFiles = 0
        self.setup_social_media_info()

    def set_website_dict(self, url_link, window_handles):
        website_name = url_link.split('.')[1]
        self.multi_tab_dic[website_name] = (url_link, window_handles)

    def open_multi_tabs(self):
        self.browser.get(self.pages_url[0])
        self.set_website_dict(self.pages_url[0], self.browser.window_handles[0])
        for index in range(1, len(self.pages_url), 1):
            window_handles = GeckoDriver.open_tab(self.browser, self.pages_url[index])
            self.set_website_dict(self.pages_url[index], window_handles[index])

    def setup_social_media_info(self):
        try:
            if "instagram" in self.multi_tab_dic:
                self.insScraper = instScraper.InstagramScraper(self.browser, self.driver_type)

            if "facebook" in self.multi_tab_dic:
                self.faceScraper = facScraper.FacebookScraper(self.browser, self.driver_type)

            if "pinterest" in self.multi_tab_dic:
                self.pintScraper = pinScraper.PinterestScraper(self.browser)

            if "twitter" in self.multi_tab_dic:
                self.twitScraper = twtScraper.TwitterScraper(self.browser)

        except Exception as e:
            Ex.print_exception(e)

    def check_login_multi_tabs(self):
        try:

            if "instagram" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['instagram'][1])
                if not self.insScraper.check_instagram_login():
                    print("instagram check login Error")
                    return False

            if "facebook" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['facebook'][1])
                if not self.faceScraper.check_facebook_login():
                    print("facebook check login Error")
                    return False

            if "pinterest" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['pinterest'][1])
                if not self.pintScraper.check_pinterest_login():
                    print("pinterest check login Error")
                    return False

            if "twitter" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['twitter'][1])
                if not self.twitScraper.check_twitter_login():
                    print("twitter check login Error")
                    return False

            return True
        except Exception as e:
            Ex.print_exception(e)
            return False

    def login_multi_tabs(self):
        try:
            if "instagram" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['instagram'][1])
                self.insScraper.instagram_login()

            if "facebook" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['facebook'][1])
                self.faceScraper.facebook_login()
                page_name = "JMS CR Gallery"
                self.faceScraper.go_facebook_page(page_name)

            if "pinterest" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['pinterest'][1])
                self.pintScraper.pinterest_login()

            if "twitter" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['twitter'][1])
                self.twitScraper.twitter_login()

        except Exception as e:
            Ex.print_exception(e)

    def post(self, file_path):
        try:
            if "instagram" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['instagram'][1])
                description = ""
                self.insScraper.share(file_path, description)

            if "facebook" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['facebook'][1])
                description = ""
                self.faceScraper.post(file_path, description)

            if "pinterest" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['pinterest'][1])
                board_name = ""
                description = ""
                self.pintScraper.pin(file_path, board_name, description)

            if "twitter" in self.multi_tab_dic:
                self.browser.switch_to_window(self.multi_tab_dic['twitter'][1])
                description = ""
                self.twitScraper.tweet(file_path, description)

        except Exception as e:
            Ex.print_exception(e)

    def post_all_files_in_source_folder(self):
        try:
            index = 0
            while self.__remainingFiles != 0:
                self.post(self.files[index])
                self.__remainingFiles = len(self.files) - self.__fileIterator
                Utl.move_file(self.files[index])
                index += 1
                TimeSteps.time_between_posts(30, 60)

        except Exception as e:
            Ex.print_exception(e)

    def __exit__(self):
        self.__close_driver()

    def __close_driver(self):
        self.browser.close()