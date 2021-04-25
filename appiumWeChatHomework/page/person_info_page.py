import sys

from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.edit_person_info_page import EditPersonInfoPage


class PersonInfoPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/person_info_page.yml"

    def edit_person_info(self):
        # 点击 编辑，
        # //*[@text="个人信息"]/../../../../../android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return self

    def edit_member(self):
        # 点击 编辑成员 链接，转向 编辑成员页面 edit_person_info_page
        # //*[@text="编辑成员"]
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return EditPersonInfoPage(self._driver)
