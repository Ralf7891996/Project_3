#реализуем логгирование
import logging

_log_format = f"%(asctime)s [%(levelname)s] %(message)s"


#Функция создает файл x.log и записывает в него логи в соотвествии с форматом


def get_file_handler():
    file_handler = logging.FileHandler("logs/x.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


#Функция создает логи и передает на запись

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    return logger