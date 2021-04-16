from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    """
    ActionChains 事件：鼠标点击，双击，右键点击
    """
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        elm_clc = self.driver.find_element(By.XPATH, '//*[@value="click me"]')
        elm_dbl_clc = self.driver.find_element(By.CSS_SELECTOR, 'input[value="dbl click me"]')
        elm_right_clc = self.driver.find_element(By.CSS_SELECTOR, 'input[value="right click me"]')

        action = ActionChains(self.driver)
        action.click(elm_clc)
        action.double_click(elm_dbl_clc)
        action.context_click(elm_right_clc) #这是右键点击
        action.perform()
        sleep(3)

    """
        ActionChains: 鼠标移动到定位的元素
    """
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        elm_moveto =self.driver.find_element_by_id("s-usersetting-top") #页面上方的“设置”链接

        action = ActionChains(self.driver)
        action.move_to_element(elm_moveto)
        action.perform()
        sleep(3)

    """
    ActionChains: 模拟拖拽元素
    """
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_el = self.driver.find_element_by_id("dragger")
        drop_el = self.driver.find_element_by_xpath('.//div[text()="Item 2"]')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag_el,drop_el).perform()
        #action.click_and_hold(drag_el).release(drop_el).perform()
        #action.click_and_hold(drag_el).move_to_element(drop_el).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        el = self.driver.find_element_by_css_selector("body>label input")

        el.click()
        action = ActionChains(self.driver)
        action.send_keys("abcdefg").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(3)