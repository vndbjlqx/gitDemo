import sys

from appium.webdriver import WebElement

from appiumWeChatHomework.page.add_friend_page import AddFriendPage
from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.search_page import SearchPage


class ContactListPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/contact_list_page.yml"

    def search(self):
        # 点击 搜索 按钮，转向 搜索页面 search_page
        # //*[@text="刘群星企业微信"]/../../../../../android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return SearchPage(self._driver)

    def goto_add_friend_page(self):
        # 点击 添加成员 按钮， 转向 添加成员页面 add_friend_page
        # //*[@text='添加成员']
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return AddFriendPage(self._driver)

    def get_contact_list(self):
        # 返回所有成员 list
        # //*[@text='企业通讯录']/../..//android.widget.TextView
        elements: list[WebElement] = self.steps(self.file_path, sys._getframe().f_code.co_name)
        contact_names = []
        for el in elements:
            contact_names.append(el.text)
        return contact_names
