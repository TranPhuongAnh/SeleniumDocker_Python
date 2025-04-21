from selenium import webdriver
import os

from src.main.config.DriverType import DriverType
from src.main.config.FileReaderManager import FileReaderManager
from src.main.config.EnvironmentType import EnvironmentType
from src.main.config.Chrome_config import ChromeConfiguration
from src.main.config.Firefox_config import FirefoxConfiguration
from src.main.config.Safari_config import SafariConfiguration
from src.main.config.Edge_config import EdgeConfiguration

class DriverManager:
    driver = None
    def __init__(self):
        self.driver_type = FileReaderManager.getInstance().get_config_reader().getBrowser()
        self.environment_type = FileReaderManager.getInstance().get_config_reader().getEnvironment()

    def webdriver_options(self):
        if self.driver_type == DriverType.CHROME:
            return ChromeConfiguration.chrome_options()
        elif self.driver_type == DriverType.FIREFOX:
            return FirefoxConfiguration.firefox_options()
        elif self.driver_type == DriverType.EDGE:
            return EdgeConfiguration.edge_options()
        elif self.driver_type == DriverType.SAFARI:
            return SafariConfiguration.safari_options()

    def connect_to_grid(self):
        # Kết nối tới Selenium Grid
        hub_host = os.getenv("HUB_HOST", "localhost")
        grid_url = f"http://{hub_host}:4444/wd/hub"
        print(f"Đang kết nối tới Selenium Grid tại {grid_url}...")

    def create_local_driver(self):
        if self.driver_type == DriverType.CHROME:
            self.driver = webdriver.Chrome()
        elif self.driver_type == DriverType.FIREFOX:
            self.driver = webdriver.Firefox()
        elif self.driver_type == DriverType.EDGE:
            self.driver = webdriver.Edge()
        elif self.driver_type == DriverType.SAFARI:
            self.driver = webdriver.Safari()

        return self.driver

    def create_driver(self):
        global driver
        if self.environment_type == EnvironmentType.LOCAL:
            self.driver = self.create_local_driver()
        elif self.environment_type == EnvironmentType.DOCKER:
            self.driver = webdriver.Remote(
                command_executor = self.connect_to_grid(),
                options= self.webdriver_options()
            )
        else:
            raise Exception("Không tìm thấy môi trường!")

        return self.driver

    def get_driver(self):
        if (self.driver is None):
            self.driver = self.create_driver()

        return self.driver

    def quit_driver(self):
        self.driver.quit()