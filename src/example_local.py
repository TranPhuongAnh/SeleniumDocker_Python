from selenium import webdriver
from selenium.webdriver.chrome.options import Options

grid_url = "http://localhost:4444/wd/hub"
print(f"Đang kết nối tới Selenium Grid tại {grid_url}...")

chrome_options = Options()
chrome_options.browser_version = "latest"
chrome_options.platform_name = "ANY"

driver = webdriver.Remote(
    command_executor=grid_url,
    options=chrome_options
)

driver.get("https://dantri.com.vn/")
print("Trang đã load:", driver.title)
driver.quit()
