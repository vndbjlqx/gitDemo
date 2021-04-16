from selenium.webdriver import ActionChains
from time import sleep
from Base import Base


class TestAlert(Base):

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到frame框架
        self.driver.switch_to.frame("iframeResult")
        drag_el = self.driver.find_element_by_id("draggable")
        drop_el = self.driver.find_element_by_id('droppable')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag_el, drop_el).perform()
        sleep(3)

        # 重点在这里 --> 点击 alert 确认 ，<-- 重点在这里。
        self.driver.switch_to.alert.accept()
        #self.driver.switch_to.alert.dismiss() #取消
        sleep(2)

        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)