import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.main.config.DriverManager import DriverManager

def run_test_on_grid():
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    try:
        # Truy cập trang Wikipedia
        driver.get("https://vi.wikipedia.org")
        print(f"Tiêu đề trang: {driver.title}")

        # Kiểm tra URL hiện tại
        wait = WebDriverWait(driver, 10)

        # Tìm kiếm
        print("Đang chờ ô tìm kiếm...")
        search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='search']")))
        print("Tìm thấy ô tìm kiếm, đang nhập từ khóa...")
        search_box.clear()
        search_box.send_keys("Selenium (phần mềm)")
        print("Đang chờ nút tìm kiếm...")
        btn_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='cdx-button cdx-search-input__end-button']")))
        print("Đã tìm thấy nút tìm kiếm, đang click...")
        btn_search.click()

        # Chọn bai viết đầu tiên
        print("Đang chờ bài viết đầu tiên...")
        first_article = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mw-content-text']/div[3]/div[3]/ul/li[1]")))
        print("Click vào bài viết đầu tiên...")
        first_article.click()

        # Đợi kết quả
        time.sleep(3)

        # Lấy tiêu đề bài viết
        try:
            print("Đang chờ tiêu đề bài viết...")
            article_title = wait.until(EC.element_to_be_clickable((By.ID, "firstHeading")))
            print(f"Tiêu đề bài viết: {article_title.text}")
        except:
            print("Không tìm thấy tiêu đề bài viết")

        # Lấy đoạn văn đầu tiên
        try:
            print("Đang lấy đoạn văn đầu tiên...")
            first_paragraph = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mw-parser-output > p")))
            print(f"\nĐoạn văn đầu tiên: {first_paragraph.text}")
        except:
            print("Không tìm thấy đoạn văn đầu tiên")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        driver_manager.quit_driver()

if __name__ == "__main__":
    # Đợi Selenium Grid khởi động
    time.sleep(3)
    run_test_on_grid()
