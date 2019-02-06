import os
from ptest.decorator import AfterMethod, TestClass, BeforeClass,BeforeMethod
from Utils.Driver import Driver
import yaml
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




    #
    # '''
    # environment = "staging" to change the environment.
    # it could be "staging", "live"
    #
    # country value could be 'cn' or 'sg'.
    # os.environ['environment'] = 'qa'
    # os.environ['country'] = 'cn'
    # os.environ['school_type'] = 'own'
    # '''

# @TestClass()
# class ProjectBase():
#     @staticmethod
#     def get_relative_path(path, file_name):
#         return os.path.join(os.path.dirname(__file__), path, file_name)
#
#     @BeforeClass()
#     def set_environment_configuration(self):
#         config_file = self.get_relative_path("./", "configuration.yml")
#         with open(config_file, 'r') as f:
#             yaml_config = yaml.load(f)
#             self.user_name = yaml_config["user_name"]
#             self.password = yaml_config['pwd']
#             self.url = yaml_config['url']
#
#     @BeforeMethod()
#     def launch_browser(self):
#         config_file = self.get_relative_path("", "env_settings")
#         with open(config_file, 'r') as f:
#             yaml_config = yaml.load(f)
#             browser_name = yaml_config['browser']
#             chrome_driver_path = yaml_config['chrome_driver']
#         if browser_name == "Chrome":
#             chrome_driver = chrome_driver_path.replace(
#                 "~", os.path.expanduser('~'))
#             self.dirver = Driver()
#
#         if browser_name == "Firefox":
#             self.driver = Driver()