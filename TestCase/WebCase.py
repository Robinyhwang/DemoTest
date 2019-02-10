from time import sleep
import requests
from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from PageObject.ArticlePage import ArticlePage
# from PageObject.LoginPage import LoginPage
from ptest.decorator import TestClass, Test
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utils.Driver import Driver


@TestClass()
class WebTestCase(Driver):

    @Test()
    def test_open_home_page(self):
        driver=Driver().start()
        homepage = HomePage(driver)

        # homepage.advertisement_close()
        homepage.login_link_click()
        loginpage = LoginPage(driver)
        loginpage.login()
        assert (homepage.username_display.is_displayed())
        assert(homepage.main_image.is_displayed())
        homepage.main_article_click()
        articlepage= ArticlePage(driver)
        assert(driver.title)
        assert(articlepage.headline == homepage.main_article_text)
        assert(articlepage.main_image().is_displayed())




    # def __init__(self):
    #     self.driver= webdriver.Chrome()
    #
    #
    # def check_advertise_and_close(self):
    #     advertise=(By.ID,'celtra-object-235')
    #     try:
    #         WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(advertise))
    #         close_button=self.driver.find_element_by_id('celtra-object-235')
    #         close_button.click()
    #     except:
    #         pass
    #
    # def login(self):
    #     login_link= self.driver.find_element_by_class_name('nav-login')
    #     login_link.click()
    #     sleep(3)
    #     username=self.driver.find_element_by_id('j_username')
    #     password=self.driver.find_element_by_id('j_password')
    #     signin_btn=self.driver.find_element_by_class_name('btn')
    #     username.send_keys('digitaltest10')
    #     password.send_keys('Sphdigital1')
    #     signin_btn.click()
    #
    # def verify_login(self):
    #     username_after_login=self.driver.find_element_by_class_name("nav-user")
    #     assert (username_after_login.is_displayed())
    #
    # def main_article(self):
    #     main_article=self.driver.find_element_by_class_name('block-link')
    #     main_article_image=self.driver.find_element_by_xpath("//div[@class='media-single']/ul[1]/li[1]/div[1]")
    #     assert(main_article_image.is_displayed())
    #     title=main_article.text()
    #     main_article.click()
    #     in_main_article_text=self.driver.find_element_by_class_name('headline node-title').text
    #     assert(title==in_main_article_text)
    #     in_main_article_images=self.driver.find_elements_by_class_name('media-entity')
    #     assert(in_main_article_images is True)


