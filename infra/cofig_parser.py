from os.path import dirname , realpath
import yaml


class ConfigParser:
    configFile = "{}\..\config\config.yaml".format(dirname(realpath(__file__)))

    @classmethod
    def parse(self, types, with_config=False):
        ret = None
        with open(ConfigParser.configFile, 'r') as stream:
            config = yaml.safe_load(stream)
            url = "{}://{}:{}".format(config['server']['schema'], config['server']['host'], config['server']['port'])

            if not isinstance(types, list):
                ret = types(url)
            else:
                ret = [t(url) for t in types]

            if with_config:
                return ret, config

            return ret



