from selenium.webdriver.safari.options import Options

class SafariConfiguration:
    def safari_options(self):
        # Thiết lập Firefox options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--start-maximized")
        return options