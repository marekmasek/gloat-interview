import json
from json import JSONDecodeError
from pathlib import Path

from exceptions.exceptions import TestDataConfigurationException

CONFIG_PATH = "data/environment/{}.json"


class TestData:
    env: str
    apiBaseUrl: str
    apiKey: str
    baseUrl: str
    seleniumTimeout: float

    @staticmethod
    def load_test_data(env: str):
        print(f"Running tests on env: {env}")
        TestData.env = env

        path = Path(__file__).absolute().parent.parent / CONFIG_PATH.format(env)
        try:
            with open(path) as config_file:
                config_data = json.load(config_file)
                TestData._load_property(config_data, 'apiBaseUrl')
                TestData._load_property(config_data, 'apiKey')
                TestData._load_property(config_data, 'baseUrl')
                TestData._load_property(config_data, 'seleniumTimeout')
        except FileNotFoundError:
            raise TestDataConfigurationException(
                f"Test data json file for env: '{env}' doesn't exist in path: '{path.absolute()}'")
        except JSONDecodeError as e:
            raise TestDataConfigurationException(
                f"Error loading test data json file for env: '{env}' in path: '{path.absolute()}', because of: {str(e)}"
            )

    @staticmethod
    def _load_property(config_data, name: str):
        if name not in config_data or config_data[name] is None:
            raise TestDataConfigurationException(
                f"Variable '{name}' is missing/misspelled/null in the test data json file for env: '{TestData.env}'")
        setattr(TestData, name, config_data[name])
