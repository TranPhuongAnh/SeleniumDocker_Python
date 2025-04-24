import time
from selenium.webdriver.common.by import By
from behave import given, when, then, step
from src.main.config.DriverManager import DriverManager


class seacrh_exam:
    """Hàm chính thực hiện các thao tác Selenium."""
    @given('Create a new browser instance')
    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()

    @step('I navigate to Google')
    def go_to_google(self):
        # Truy cập Google
        self.driver.get('https://www.google.com')
        print(f"Tiêu đề trang: {self.driver.title}")

    @when('I search for "{search_query}"')
    def search_data_in_website(self):
        # Tìm kiếm
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('Selenium Docker Python')
        search_box.submit()

        # Đợi kết quả tìm kiếm xuất hiện
        time.sleep(2)

        # In tiêu đề trang kết quả tìm kiếm
        assert self.driver.title == "Selenium Docker Python - Google Search"
        print(f"Tiêu đề sau khi tìm kiếm: {self.driver.title}")

    @then('I should see the search results')
    def get_search_result(self):
        # Lấy các kết quả tìm kiếm
        search_results = self.driver.find_elements(By.CSS_SELECTOR, 'h3')
        print("\nKết quả tìm kiếm:")
        for i, result in enumerate(search_results[:5], 1):
            print(f"{i}. {result.text}")

    @step('Search: Close Browser')
    def close_browser(self):
        self.driver_manager.quit_driver()
        print("Đóng trình duyệt...")

