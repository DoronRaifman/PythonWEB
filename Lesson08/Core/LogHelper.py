
import logging
import os
from logging.handlers import RotatingFileHandler


def configure_log(use_console=True, name="App", folder='log', logger_name=None,
                  level=logging.DEBUG,
                  message_format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(funcName)s(): %(message)s'):
    date_format = "%y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(fmt=message_format, datefmt=date_format)
    os.makedirs(folder, exist_ok=True)
    log_file = os.path.join(folder, '%s.log' % name)
    file_handler = RotatingFileHandler(log_file, mode='w', encoding='utf8', maxBytes=1000000, backupCount=3)
    file_handler.setLevel(level)  # TODO from config
    handlers = [file_handler]
    if use_console:
        console_handler = logging.StreamHandler()
        handlers.append(console_handler)
        console_handler.setLevel(level)
    logger = logging.getLogger() if logger_name is None else logging.getLogger(logger_name)
    logger.setLevel(level)  # TODO from config
    for h in handlers:
        h.setFormatter(formatter)
    logger.handlers = handlers
    # logger.addHandler(h)
    return logger

