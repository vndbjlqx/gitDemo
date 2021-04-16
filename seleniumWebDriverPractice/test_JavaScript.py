import pytest

from Base import Base
from time import sleep

class TestJavaScript(Base):

    """
    selenium 执行JavaScript的代码，获得元素，与滚动屏幕
    """
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        el = self.driver.execute_script("return document.getElementById('su')")
        el.click()

        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_link_text("下一页 >").click()
        sleep(3)

        for code in ["return document.title",
                     "return JSON.stringify(performance.timing)"]:
            print(self.driver.execute_script(code))

        #下面的语句只会执行第一个return后的语句，就返回了。
        #self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)")

    """
        javascript 操纵日期空间
    """
    def test_datetimer(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(6)
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly');")
        sleep(1)
        self.driver.execute_script("document.getElementById('train_date').value=''")
        sleep(1)
        self.driver.execute_script("document.getElementById('train_date').value='2021-04-20'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))








