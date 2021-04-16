from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:
    def setup(self):
        self.driverpath ="E:\softwares\geckodriver-v0.29.1-win64\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=self.driverpath)
        #self.driver = webdriver.Chrome() 已经设置过系统Path，所以，不用再加载路径
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_xpath("//a[@href='/topics/29255']").click()
        #self.driver.find_element(By.ID,"123")