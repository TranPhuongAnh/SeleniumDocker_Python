from src.main.config.DriverType import DriverType
from src.main.config.EnvironmentType import EnvironmentType


class ConfigFileReader:
    propertyFilePath = ("config/config.properties")
    def __init__(self):
        self.property_file_path = self.propertyFilePath
        self.properties = {}

        try:
            with open(self.property_file_path, "r", encoding="utf-8") as reader:
                for line in reader:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        self.properties[key.strip()] = value.strip()
        except FileNotFoundError:
            raise RuntimeError(f"Configuration.properties not found at {self.property_file_path}")
        except Exception as e:
            print("Đã xảy ra lỗi khi đọc file config:")
            print(e)

    def get_property(self, key: str, default=None):
        return self.properties.get(key, default)

    def read_properties_file(self):
        config = {}
        with open(self.propertyFilePath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=")
                    config[key.strip()] = value.strip()
        return config

    def getBrowser(self):
        reader = self.read_properties_file()
        self.browserName = reader["browser"]
        if (self.browserName is None or self.browserName.lower() == "chrome"):
            return DriverType.CHROME
        elif (self.browserName.lower() == "firefox"):
            return DriverType.FIEREFOX
        elif (self.browserName.lower() == "edge"):
            return DriverType.EDGE
        elif (self.browserName.lower() == "safari"):
            return DriverType.SAFARI
        else:
            print("Chưa cấu hình browser, mặc định sử dụng Chrome Browser!")
            return DriverType.CHROME

    def getEnvironment(self):
        reader = self.read_properties_file()
        self.environmentName = reader["environment"]
        if(self.environmentName is None or self.environmentName.lower() == "local"):
            return EnvironmentType.LOCAL
        elif(self.environmentName.lower() == "docker"):
            return EnvironmentType.DOCKER
        else:
            print("Chưa cấu hình môi trường, mặc định là DOCKER")
            return EnvironmentType.DOCKER