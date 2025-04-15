import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

def take_screenshot():
    """Truy cập một trang web và chụp ảnh màn hình."""
    # Thiết lập Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')

    # Khởi tạo driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Truy cập trang web
        url = "https://www.python.org"
        print(f"Đang truy cập {url}...")
        driver.get(url)

        # Đợi để trang load hoàn chỉnh
        time.sleep(2)

        # Lấy tiêu đề trang
        title = driver.title
        print(f"Tiêu đề trang: {title}")

        # Tìm các menu chính
        menus = driver.find_elements(By.CSS_SELECTOR, '.main-navigation ul.navigation-list li')
        print("\nCác menu chính:")
        for menu in menus:
            print(f"- {menu.text}")

        # Tìm kiếm trên trang
        search_box = driver.find_element(By.ID, 'id-search-field')
        search_term = "selenium"
        search_box.send_keys(search_term)
        search_box.submit()

        # Đợi kết quả tìm kiếm
        time.sleep(2)

        # Chụp ảnh màn hình
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshot_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Đã chụp ảnh màn hình: {screenshot_path}")

        # Lấy kết quả tìm kiếm
        results = driver.find_elements(By.CSS_SELECTOR, '.list-recent-events li')
        print("\nKết quả tìm kiếm cho '{}':".format(search_term))
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    take_screenshot()
