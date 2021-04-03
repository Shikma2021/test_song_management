import configparser
import inspect
from os.path import dirname , join , realpath
import yaml

CONFIG_DIR_NAME = "config"

class ConfigParser:
    configFile = "{}\..\config\config.yaml".format(dirname(realpath(__file__)))

    @classmethod
    def parse(self, types):
        #url = "http://127.0.0.1:3002"
        with open(ConfigParser.configFile, 'r') as stream:
            config = yaml.safe_load(stream)
            url = "{}://{}:{}".format(config['server']['schema'], config['server']['host'], config['server']['port'])

            if not isinstance(types, list):
                return types(url)
            else:
                return [t(url) for t in types]
