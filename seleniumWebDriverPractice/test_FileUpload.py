from Base import Base
from time import sleep

class TestFileUpload(Base):


    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        #self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        #应该是不用点 上传按钮，直接send_keys就可以了
        el = self.driver.find_element_by_id("stfile")
        #注意这里一定要用绝对路径。
        el.send_keys("E:\PycharmProjects\\testPytestDemo\\testWebDriverSelenium\pic\ship.jpg")
        sleep(3)