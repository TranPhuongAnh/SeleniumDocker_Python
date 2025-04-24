import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step

from src.main.config.DriverManager import DriverManager

class grid_example:
    @given('Wiki: I create a new WebDriver')
    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()
        self.wait = WebDriverWait(self.driver, 10)

    @when('Wiki: I go to Wikipedia')
    def go_to_Wikipedia(self):
            self.driver.get("https://vi.wikipedia.org")
            self.driver.timeouts(3).implicitly_wait(20)
            # Kiểm tra tiêu đề trang
            assert self.driver.title == 'Wikipedia', f'Expected title to be "Wikipedia", but got "{self.driver.title}"'
            print(f'Tiêu đề trang: {self.driver.title}')


    @when('Wiki: I search data in website')
    def search_data_in_website(self):
        print("Đang chờ ô tìm kiếm...")
        search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search']")))
        print("Tìm thấy ô tìm kiếm, đang nhập từ khóa...")
        search_box.clear()
        search_box.send_keys("Selenium (phần mềm)")
        print("Đang chờ nút tìm kiếm...")
        btn_search = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='cdx-button cdx-search-input__end-button']")))
        print("Đã tìm thấy nút tìm kiếm, đang click...")
        btn_search.click()

    @then('Wiki: I select the first article')
    def select_first_article(self):
        print("Đang chọn bài viết đầu tiên...")
        first_article = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mw-content-text']/div[3]/div[3]/ul/li[1]")))
        print("Click vào bài viết đầu tiên")
        first_article.click()

        # Đợi kết quả
        time.sleep(3)

    @step('Wiki: I get article title and first paragraph')
    def get_article_title(self):
        print("Đang chờ tiêu đề bài viết...")
        article_title = self.wait.until(EC.element_to_be_clickable((By.ID, "firstHeading")))
        print(f"Tiêu đề bài viết: {article_title.text}")

        # Lấy đoạn văn đầu tiên
        try:
            print("Đang lấy đoạn văn đầu tiên...")
            first_paragraph = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mw-parser-output > p")))
            print(f"\nĐoạn văn đầu tiên: {first_paragraph.text}")
        except:
            print("Không tìm thấy đoạn văn đầu tiên")

    @step('Wiki: I close the browser')
    def close_browser(self):
        self.driver.quit()