from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Utils.Driver import Driver


class HomePage():
    def __init__(self, driver):
        self.driver=driver

    # def __init__(self):
    #     super().__init__()

    __login_link = 'nav-login'
    __close_button = '#celtra-object-118'
    __username="nav-user"
    __headline="//span[contains(@class,'story-headline')]/a[1]"
    def get_url(self,url):
        return self.driver.start(url)



    def login_link_click(self):
        return self.driver.find_element(By.CLASS_NAME, self.__login_link).click()



    def advertisement_close(self):
        try:
            fr=self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[13]/iframe[1]")
            self.driver.switch_iframe(fr)
            self.driver.find_element(By.CSS_SELECTOR, self.__close_button).click()
        except NoSuchElementException:
            self.driver.find_element(By.CLASS_NAME, self.__login_link)

    @property
    def username_display(self):
        username_after_login = self.driver.find_element(By.CLASS_NAME, self.__username)
        return username_after_login
    @property
    def main_article_text(self):
        return self.driver.find_element(By.XPATH, self.__headline).text


    @property
    def main_image(self):
        return self.driver.find_element_by_xpath("//img[@class='borealis image-style-retina_large borealis-js img-responsive']")

    def main_article_click(self):
        self.driver.find_element(By.CLASS_NAME,'block-link').click()

    def main_article_titile(self):
        self.driver.find_element_by_xpath("//div[@class='media-single']/ul[1]/li[1]/div[1]")

