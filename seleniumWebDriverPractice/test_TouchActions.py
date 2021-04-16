from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchActions:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    """
       TouchActions:输入，点击，向下滚动窗口 
    """
    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        #scroll滚动屏幕，x=0,水平方向不滚动; y=10000,竖直方向向下滚动10000
        action.scroll_from_element(el,0,10000).perform()
        sleep(3)
