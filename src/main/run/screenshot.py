import os
import time
from pathlib import Path

from selenium.webdriver.common.by import By
from datetime import datetime

from src.main.config.DriverManager import DriverManager

def take_screenshot():
    """Truy cập một trang web và chụp ảnh màn hình."""
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()

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
        menus = driver.find_elements(By.XPATH, '//*[@id="mainnav"]/ul/li')
        print("\nCác menu chính:")
        print("pass 1")
        for menu in menus:
            print(f"- {menu.text}")

        # Tìm kiếm trên trang
        search_box = driver.find_element(By.ID, 'id-search-field')
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
