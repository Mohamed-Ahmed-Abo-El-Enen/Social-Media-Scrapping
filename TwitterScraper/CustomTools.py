from selenium.webdriver.common.keys import Keys


def press_page_down(browser):
    browser.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)




