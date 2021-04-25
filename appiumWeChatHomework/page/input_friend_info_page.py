import sys

from appiumWeChatHomework.page.base_page import BasePage


class InputFriendInfoPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/input_friend_info_page.yml"

    def input_friend_info(self, name, phone):
        # 录入：姓名，手机号
        # //*[*[contains(@text,"姓名")]]/*[contains(@class,"EditText")]
        # // *[*[contains( @ text, "手机")]]//android.widget.EditText
        self._params["friend_name"] = name
        self._params["friend_phone"] = phone
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return self

    def save(self):
        # 点击 保存 按钮，转向 添加成员页面 add_friend_page
        # //*[@text='保存']
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        from appiumWeChatHomework.page.add_friend_page import AddFriendPage
        return AddFriendPage(self._driver)
