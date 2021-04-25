import sys
from time import sleep

from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.input_friend_info_page import InputFriendInfoPage


class AddFriendPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/add_friend_page.yml"

    def goto_manual_add_friend_page(self):
        # 点击 手动输入添加 按钮，转向 录入成员信息页面
        # //*[@text='手动输入添加']
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return InputFriendInfoPage(self._driver)

    def back(self):
        # 点击 返回 按钮，返回  通讯录页面 contact_list_page
        # //*[@text="添加成员"]/../../../../android.widget.TextView
        sleep(3)
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        from appiumWeChatHomework.page.contact_list_page import ContactListPage
        return ContactListPage(self._driver)
