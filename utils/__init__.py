import os

from models.app_model import AppConfig
from utils.file_utils import load_configuration
from utils.logger_utils import setup_custom_logger

app_config = load_configuration(config_model=AppConfig, path_to_load_from=os.getenv("conf_path"))
logger = setup_custom_logger(app_config.logger)
