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
    __close_button = 'celtra-object-118'
    __username="nav-user"
    def get_url(self,url):
        return self.driver.start(url)



    def login_link_click(self):
        return self.driver.find_element(By.CLASS_NAME, self.__login_link).click()



    def advertisement_close(self):
        try:
            iframe=self.driver.find_element_by_xpath("//iframe[contains(@frameborder,'0')]")
            self.driver.switch_iframe(iframe)

            self.driver.find_element(By.ID, self.__close_button).click()

        except NoSuchElementException:
            self.driver.find_element(By.CLASS_NAME, self.__login_link)

    @property
    def username_display(self):
        username_after_login = self.driver.find_element(By.CLASS_NAME, self.__username)
        return username_after_login

    def main_article(self):
        main_article=self.driver.find_element_by_class_name('block-link')
        main_article_image=self.driver.find_element_by_xpath("//div[@class='media-single']/ul[1]/li[1]/div[1]")
        assert(main_article_image.is_displayed())
        title=main_article.text()
        main_article.click()
        in_main_article_text=self.driver.find_element_by_class_name('headline node-title').text
        assert(title==in_main_article_text)
        in_main_article_images=self.driver.find_elements_by_class_name('media-entity')
        assert(in_main_article_images is True)

    def main_image(self):
        self.driver.find_element_by_xpath("//div[@class='media-single']/ul[1]/li[1]/div[1]")

    def main_article_click(self):
        self.driver.find_element(By.CLASS_NAME,'block-link')

    def main_article_titile(self):
        self.driver.find_element_by_xpath("//div[@class='media-single']/ul[1]/li[1]/div[1]")

