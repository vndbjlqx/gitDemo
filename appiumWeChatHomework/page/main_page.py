import sys

from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.contact_list_page import ContactListPage


class MainPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/main_page.yml"

    def goto_contact_list_page(self):
        # 点击，通讯录， 转向 通讯录页面 contact_list_page
        # //*[@text='通讯录']
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return ContactListPage(self._driver)

    def goto_msg_page(self):
        # 点击，信息， 返回主页面
        # .//*[@text="消息"]
        self.steps(self.file_path, sys._getframe().f_code.co_name)