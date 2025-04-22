import time
from selenium.webdriver.common.by import By

from src.main.config.DriverManager import DriverManager


def main():
    """Hàm chính thực hiện các thao tác Selenium."""
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()

    try:
        print("Bắt đầu tự động hóa browser...")

        # Truy cập Google
        driver.get('https://www.google.com')
        print(f"Tiêu đề trang: {driver.title}")

        # Tìm kiếm
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys('Selenium Docker Python')
        search_box.submit()

        # Đợi kết quả tìm kiếm xuất hiện
        time.sleep(2)

        # In tiêu đề trang kết quả tìm kiếm
        print(f"Tiêu đề sau khi tìm kiếm: {driver.title}")

        # Lấy các kết quả tìm kiếm
        search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        print("\nKết quả tìm kiếm:")
        for i, result in enumerate(search_results[:5], 1):
            print(f"{i}. {result.text}")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        print("Đóng trình duyệt...")
        driver_manager.quit_driver()

if __name__ == "__main__":
    main()
