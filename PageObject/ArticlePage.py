from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Utils.Driver import Driver


class ArticlePage():

    def __init__(self, driver):
        self.driver=driver

    # def __init__(self):
    #     super().__init__()

    __headline = 'headline node-title'
    __main_image="//picture[@class='img-responsive']//img[@class='img-responsive']"
    @property
    def headline(self):
        return self.driver.find_element(By.CLASS_NAME,self.__headline).text

    def main_image(self):
        return self.driver.find_element(By.XPATH, self.__main_image)
