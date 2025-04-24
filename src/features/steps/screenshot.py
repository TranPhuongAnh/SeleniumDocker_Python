import os
import time
from pathlib import Path
from selenium.webdriver.common.by import By
from datetime import datetime
from behave import given, when, then, step

from src.main.config.DriverManager import DriverManager

class screenshot:
    """Class này chứa các hàm liên quan đến việc chụp ảnh màn hình trong quá trình test."""
    @given("Create driver")
    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()

    @step("Open web browser")
    def open_web_browser(self):
        # Truy cập trang web
        url = "https://www.python.org"
        print(f"Đang truy cập {url}...")
        self.driver.get(url)

        # Đợi để trang load hoàn chỉnh
        time.sleep(2)

    @step("Check title page")
    def check_title_page(self):
        # Lấy tiêu đề trang
        title = self.driver.title
        print(f"Tiêu đề trang: {title}")
        expect_title = "Welcome to Python.org"
        assert(title,expect_title)
        print("Tiêu đề trang chính xác")

    @when("Search data in website")
    def search_data_in_website(self):
        # Tìm các menu chính
        menus = self.driver.find_elements(By.XPATH, '//*[@id="mainnav"]/ul/li')
        print("\nCác menu chính:")
        print("pass 1")
        for menu in menus:
            print(f"- {menu.text}")

        # Tìm kiếm trên trang
        search_box = self.driver.find_element(By.ID, 'id-search-field')
        # Dữ liệu nhập sẵn
        search_term = "python"
        # Nhập dữ liệu trực tếp để tìm kiếm
        key = input("Nhập từ khóa cần tìm kiếm: ")
        search_box.send_keys(key)
        search_box.submit()
        print(f"Tìm kiếm '{key}'...")

        # Đợi kết quả tìm kiếm
        time.sleep(2)
        print("Chờ 2s")

        # Lấy kết quả tìm kiếm
        results = self.driver.find_elements(By.CSS_SELECTOR, '.list-recent-events li')
        print("\nKết quả tìm kiếm cho '{}':".format(key))
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")

    @then("Take screenshot search result")
    def take_screenshot(self):
        try:
            # Lấy đường dẫn đến file đang chạy
            current_file = Path(__file__).resolve()
            project_folder = current_file.parents[3]
            print("File đang chạy:", current_file)
            print("Thư mục dự án:", project_folder)

            # Tạo thư mục nếu chưa có
            folder_path = f"{project_folder}/data/screenshots"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Đặt tên file ảnh
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(folder_path, f"screenshot_{timestamp}.png")

            # Chụp và lưu ảnh màn hình
            self.driver.save_screenshot(screenshot_path)
            print(f"Đã chụp ảnh màn hình: {screenshot_path}")

        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

    @then ("Screenshot: Close browser")
    def close_browser(self):
        self.driver_manager.quit_driver()
