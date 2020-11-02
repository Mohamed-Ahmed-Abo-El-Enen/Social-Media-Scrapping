from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def init_chrome_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 '
            '(KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        browser = webdriver.Chrome(executable_path="Assets/WebDriver/chromedriver.exe",options=chrome_options)
        return browser
    except Exception as e:
        print("Uncontrolled error: " + str(e))
        input("Press any key to continue...")
