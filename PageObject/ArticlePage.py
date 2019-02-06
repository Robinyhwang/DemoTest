from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Utils.Driver import Driver


class ArticlePage():
    def __init__(self, driver):
        self.driver=driver

    # def __init__(self):
    #     super().__init__()

    __login_link = 'nav-login'
    __close_button = 'celtra-object-118'
    __username="nav-user"