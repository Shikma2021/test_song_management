import configparser
import inspect
from os.path import dirname , join , realpath

CONFIG_DIR_NAME = "config"

class ConfigParser:

    def __init__(self):
        raise Exception("This Class is not instantiated")

    @staticmethod
    def read_configuration(config_file_name=None):
        caller_dir = dirname(inspect.getmodule(inspect.stack()[1][0]).__file__)
        config_file_name = config_file_name if config_file_name is None else config_file_name
        config_file_path = join(caller_dir,CONFIG_DIR_NAME,config_file_name)
        parser_instance = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation)
        parser_instance.read(config_file_path)
        return parser_instance

    @staticmethod
    def get_list(input_string: str , delimiter=','):
        if input_string == "":
            new_list == []
        else:
            new_list = input_string.split(delimiter)
            for index, item in enumerate(new_list):
                new_list[index] = item.strip()
        return new_list
