import yaml

from os.path import dirname

from app.decorators.method import dev_only

CONFIG_FILE = r"%s/config.yml" % dirname(__file__)


class Config:
    __overrides = dict()

    @staticmethod
    @dev_only
    def override(path: str, value: str):
        Config.__overrides[path] = value

    @staticmethod
    def get(path: str):
        if "path" in Config.__overrides:
            return Config.__overrides[path]

        with open(CONFIG_FILE) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            config = yaml.load(file, Loader=yaml.FullLoader)
            parts = path.split(".")
            result = config
            for part in parts:
                result = result[part]

            return result
