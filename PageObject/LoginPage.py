from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from Utils.Driver import Driver


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    __username = 'j_username'
    __password_button = 'j_password'
    __login_button = 'btn'

    def login_uesername(self):
        return self.driver.find_element(By.ID, self.__username).send_keys('digitaltest10')

    def login_password(self):
        return self.driver.find_element(By.ID, self.__password_button).send_keys('Sphdigital1')

    def login_button_click(self):
        return self.driver.find_element(By.CLASS_NAME, self.__login_button).click()

    def login(self):
        self.login_uesername()
        self.login_password()
        self.login_button_click()
