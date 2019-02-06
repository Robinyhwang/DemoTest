import os

import yaml
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait




class Driver(object):




        # self.driver.implicitly_wait(OVER_TIME)

    def start(self):
        config_file = self.get_relative_path("", "env_settings")
        with open(config_file, 'r') as f:
            yaml_config = yaml.load(f)
            driver_name = yaml_config['browser']
            chrome_driver_path = yaml_config['chrome_driver']
            url = yaml_config['url']
            chrome_driver = chrome_driver_path.replace(
                "~", os.path.expanduser('~'))
        if driver_name == "android":
            self.driver = webdriver.Android()
        elif driver_name == "Chrome":
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

        return self.driver


    def get_relative_path(self, path, file_name):
        return os.path.join(os.path.dirname(__file__), path, file_name)


    def find_element(self, by: By, value):
        try:

                element = self.driver.find_element(by=by, value=value)
                WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(element))

        except Exception as e:
            element = self.driver.find_element(by=by, value=value)
            print("Exception found", format(e))

    def find_elements(self, by: By, value):

            try:
                return self.driver.find_elements(by=by, value=value)
            except Exception as e:
                print("Exception found", format(e))

    # def find_display_elements(self, by: By, value):
    #
    #         try:
    #             elements = self.driver.find_elements(by=by, value=value)
    #             num = elements.__len__()
    #             if num >= 1:
    #                 break
    #             display_element = []
    #             for j in range(num):
    #                 element = elements.__getitem__(j)
    #                 if element.is_displayed():
    #                     display_element.append(element)
    #             return display_element
    #         except Exception as e:
    #             print("Exception found", format(e))
    #             time.sleep(1)

    def is_element_present(self, by: By, value):
        try:
            self.driver.find_element(by=by, value=value)
            return True
        except Exception as e:
            print("Exception found", format(e))

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def switch_iframe(self, frame):
        self.driver.switch_to.frame(frame)
    #
    # def click(self):
    #     self.driver.
