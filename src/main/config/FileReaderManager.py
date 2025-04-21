from src.main.config.ConfigFileReader import ConfigFileReader  # nếu bạn tách file

class FileReaderManager:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileReaderManager, cls).__new__(cls)
        return cls._instance

    def get_config_reader(self):
        if self._config is None:
            self._config = ConfigFileReader  # hoặc đường dẫn động
        return self._config

    @staticmethod
    def getInstance():
        return FileReaderManager()