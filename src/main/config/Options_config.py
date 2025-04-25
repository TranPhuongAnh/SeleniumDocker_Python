from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

class OptionsConfiguration:

    def chrome_options(self):
        # Thiết lập Chrome options
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')

        return options
    
    def firefox_options(self):
        # Thiết lập Firefox options
        options = FirefoxOptions()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')

        return options
    
    def edge_options(self):
        # Thiết lập Edge options
        options = EdgeOptions()
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')

        return options
    
    def safari_options(self):
        # Thiết lập Safari options
        options = SafariOptions()
        options.set_window_rect(0, 0, 1920, 1080)
        options.browser_version('latest')
        options.use_technology_preview(True)
        options.automatic_inspection(False)
        options.automatic_profiling(False)
        options.enable_downloads(False)

        return options
