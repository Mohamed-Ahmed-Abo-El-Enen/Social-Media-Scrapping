import time
from selenium.webdriver.common.keys import Keys


def press_page_down(browser):
    browser.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)


def press_end_button(browser):
    browser.find_element_by_css_selector('body').send_keys(Keys.END)


def press_arrow_down(browser):
    browser.find_element_by_css_selector('body').send_keys(Keys.ARROW_DOWN)

    def scroll_down(self, driver):
        scroll_pause_time = 0.5
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(scroll_pause_time)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height



