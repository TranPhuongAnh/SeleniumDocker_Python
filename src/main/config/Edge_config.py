from selenium.webdriver.edge.options import Options

class EdgeConfiguration:
    def edge_options(self):
        # Thiết lập Firefox options
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')