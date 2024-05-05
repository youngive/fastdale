import logging


class CustomLogger:
    def __init__(self, log_file='app.log'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Создание обработчика для записи в файл
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Добавление обработчика к логгеру
        self.logger.addHandler(file_handler)

    def log(self, message):
        # Логирование сообщения
        self.logger.info(message)
        return message
