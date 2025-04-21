from selenium.webdriver.chrome.options import Options

class ChromeConfiguration:
    def chrome_options(self):
        # Thiết lập Chrome options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
