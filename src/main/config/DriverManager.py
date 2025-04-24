import requests
from selenium import webdriver
import os

from src.main.config.DriverType import DriverType
from src.main.config.FileReaderManager import FileReaderManager
from src.main.config.EnvironmentType import EnvironmentType
from src.main.config.Options_config import OptionsConfiguration

class DriverManager:
    options = OptionsConfiguration()

    # Khởi tạo biến driver_type và environment_type
    def __init__(self):
        self.driver_type = FileReaderManager.getInstance().get_config_reader().getBrowser()
        self.environment_type = FileReaderManager.getInstance().get_config_reader().getEnvironment()

    # Lấy thông tin browser
    def webdriver_options(self):
        if self.driver_type == DriverType.CHROME:
            return self.options.chrome_options()
        elif self.driver_type == DriverType.FIREFOX:
            return self.options.firefox_options()
        elif self.driver_type == DriverType.EDGE:
            return self.options.edge_options()
        elif self.driver_type == DriverType.SAFARI:
            return self.options.safari_options()

    def is_grid_available(self, host):
        try:
            url = f"http://{host}:4444/status"
            response = requests.get(url, timeout=3)

            if response.status_code != 200:
                return False

            data = response.json()
            if 'value' in data and 'ready' in data['value']:
                return data['value']['ready']
            else:
                return False

        except Exception as e:
            return False

    # Kết nối tới Selenium Grid
    def connect_to_grid(self):
        # Kết nối tới Selenium Grid
        hub_host = os.getenv("HUB_HOST", "localhost")
        grid_url = f"http://{hub_host}:4444/wd/hub"

        if not self.is_grid_available(hub_host):
            return None

        return grid_url

    # Tạo driver cho docker
    def create_docker_driver(self):
        if self.connect_to_grid() is None:
            print("❌ Không thể kết nối tới Selenium Grid tại http://localhost:4444")
            print("👉 Vui lòng kiểm tra Docker container selenium-hub đã chạy chưa.")
            print("...... Sử dụng local để tiếp tục test! ......")

            return self.create_local_driver()
        else:
            print(f"Đang kết nối tới Selenium Grid tại {self.connect_to_grid()}...")
            self.driver = webdriver.Remote(
                command_executor = self.connect_to_grid(),
                options= self.webdriver_options()
            )
            print("✅ Selenium Grid đã sẵn sàng!")
            return self.driver

    # Tạo driver cho local
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

    # Tạo driver cho docker hoặc local
    def create_driver(self):
        global driver
        if self.environment_type == EnvironmentType.LOCAL:
            self.driver = self.create_local_driver()
        elif self.environment_type == EnvironmentType.DOCKER:
            self.driver = self.create_docker_driver()
        else:
            raise Exception("Không tìm thấy môi trường!")

        return self.driver

    def get_driver(self):
        self.driver = self.create_driver()
        self.driver.maximize_window()

        return self.driver

    # Đóng driver
    def quit_driver(self):
        print("Đang đóng trình duyệt...")
        self.driver.quit()