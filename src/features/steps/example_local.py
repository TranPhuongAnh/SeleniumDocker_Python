from src.main.config.DriverManager import DriverManager
from behave import given, when, then, step

class example_local:

    @given('Create driver for local test')
    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()

    @when('Open browser and url')
    # Open browser and URL
    def open_browser_and_url(self):
        self.driver.get("https://dantri.com.vn/")
        print("Trang đã load:", self.driver.title)

    # Check tile page
    @then('Check tile page')
    def check_tile_page(self):
        title_expected = "Tin tức Việt Nam và quốc tế nóng, nhanh, cập nhật 24h | Báo Dân trí"
        title_actual = self.driver.title
        assert title_expected == title_actual, f"Title expected: {title_expected}, Title actual: {title_actual}"
        print("Đã kiểm tra được title page đúng!")

    # Close the driver
    @step('Local: Close browser')
    def close_browser(self):
        self.driver_manager.quit_driver()
