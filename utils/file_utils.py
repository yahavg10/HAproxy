import yaml

from utils.variables_utils import ConfigModelsOptions


def load_configuration(config_model: ConfigModelsOptions, path_to_load_from: str):
    with open(file=path_to_load_from) as config_file:
        config_data = yaml.safe_load(config_file)
        return config_model.from_dict(config_data, config_model)