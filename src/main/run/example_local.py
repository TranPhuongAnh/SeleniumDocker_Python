from src.main.config.DriverManager import DriverManager

class example_local:
    def __init__(self):
        self.driver_manager = DriverManager()
        self.driver = self.driver_manager.get_driver()
    def open_browser_and_url(self):
        self.driver.get("https://dantri.com.vn/")
        print("Trang đã load:", self.driver.title)

    def close_browser(self):
        self.driver_manager.quit_driver()

if __name__ == '__main__':
    Demo = example_local()
    print("Open browser and url")
    Demo.open_browser_and_url()
    input("Press any key to exit...")
    Demo.close_browser()