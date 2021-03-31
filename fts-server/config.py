import yaml

from os.path import dirname

CONFIG_FILE = r"%s/config.yml" % dirname(__file__)


class Config:

    @staticmethod
    def get(path: str) -> str:
        with open(CONFIG_FILE) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            config = yaml.load(file, Loader=yaml.FullLoader)
            parts = path.split(".")
            result = config
            for part in parts:
                result = result[part]

            return result



