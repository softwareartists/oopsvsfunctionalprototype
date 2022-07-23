"""yaml load functions"""
import yaml


def load_yaml(file_path: str) -> dict:
    """loads yaml file from the config"""
    with open(file_path, encoding="latin1") as file_obj:
        data = yaml.safe_load(file_obj)
    return data
