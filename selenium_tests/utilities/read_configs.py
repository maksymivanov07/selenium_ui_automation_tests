import configparser
import json

from selenium_tests.utilities.configuration import Configuration


# abs_path = '/Users/max/PycharmProjects/selenium_ui_automation_tests/selenium_tests/configurations/configuration.ini'
# conf = configparser.RawConfigParser()
# conf.read(abs_path)


class ReadConfig:
    # @staticmethod
    # def get_base_url():
    #     return conf.get('app_info', 'base_url')
    #
    # @staticmethod
    # def get_login():
    #     return conf.get('user_data', 'login')
    #
    # @staticmethod
    # def get_password():
    #     return conf.get('user_data', 'password')
    #
    # @staticmethod
    # def get_browser_data():
    #     return conf.get('browser_data', 'browser_id')
    # scope = "session"

    @staticmethod
    def env():
        with open(
                '/Users/max/PycharmProjects/selenium_ui_automation_tests/selenium_tests/configurations/configuration.json') as f:
            data = f.read()
            json_to_dict = json.loads(data)
        config_json = Configuration(**json_to_dict)
        return config_json
