import yaml

from models.app_model import AppConfig


def load_configuration(config_model: AppConfig, path_to_load_from: str):
    with open(file=path_to_load_from) as config_file:
        config_data = yaml.safe_load(config_file)
        return config_model.from_dict(config_data, AppConfig)
