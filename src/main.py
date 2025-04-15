import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

def get_environment():
    """Lấy giá trị biến môi trường ENVIRONMENT hoặc mặc định là 'local'."""
    return os.environ.get('ENVIRONMENT', 'local')

def get_browser():
    """Lấy giá trị biến môi trường BROWSER hoặc mặc định là 'chrome'."""
    return os.environ.get('BROWSER', 'chrome')

def get_remote_url():
    """Lấy URL của Selenium Grid từ biến môi trường REMOTE_URL."""
    return os.environ.get('REMOTE_URL', 'http://selenium-hub:4444/wd/hub')

def create_driver():
    """Tạo và trả về một WebDriver dựa trên các thiết lập môi trường."""
    environment = get_environment()
    browser = get_browser()

    if browser.lower() == 'chrome':
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
    else:  # firefox
        options = FirefoxOptions()
        options.add_argument('--headless')

    if environment == 'remote':
        remote_url = get_remote_url()
        print(f"Connecting to remote WebDriver at {remote_url}")
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=options
        )
    elif environment == 'docker':
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Firefox(options=options)
    else:  # local
        if browser.lower() == 'chrome':
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Firefox(options=options)

    return driver

def main():
    """Hàm chính thực hiện các thao tác Selenium."""
    driver = create_driver()
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
        driver.quit()

if __name__ == "__main__":
    main()
