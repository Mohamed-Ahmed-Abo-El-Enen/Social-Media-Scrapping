from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def init_gecko_driver():
    try:
        #user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us)" \
        #             " AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        options = FirefoxOptions()
        options.log.level = "trace"
        #options.add_argument("-devtools")
        #options.add_argument("--headless")
        browser = webdriver.Firefox(executable_path="Assets/WebDriver/geckodriver.exe", firefox_profile=profile
                                    ,firefox_options=options)
        return browser
    except Exception as e:
        print("Uncontrolled error: " + str(e))
        input("Press any key to continue...")


def open_tab(driver, url_link):
    driver.execute_script("window.open('" + url_link + "');")
    return driver.window_handles


