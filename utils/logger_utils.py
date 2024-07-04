import logging

from models.logger_model import LoggerModel


def setup_custom_logger(logger_config: LoggerModel) -> logging.Logger:
    formatter = logging.Formatter(fmt=logger_config.fmt, datefmt=logger_config.datefmt)

    init_logger = logging.getLogger(name=logger_config.logger_name)
    init_logger.setLevel(logger_config.base_level)

    create_file_handler(formatter, init_logger, logger_config)
    create_stream_handler(formatter, init_logger)
    return init_logger


def create_file_handler(formatter, init_logger, logger_config):
    file_handler = logging.FileHandler(logger_config.log_file_path)
    file_handler.setFormatter(formatter)
    init_logger.addHandler(file_handler)


def create_stream_handler(formatter, init_logger):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    init_logger.addHandler(stream_handler)
