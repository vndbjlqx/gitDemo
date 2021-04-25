import sys

from appiumWeChatHomework.page.base_page import BasePage


class EditPersonInfoPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/edit_person_info_page.yml"

    def delete_person(self):
        # (向下滑动页面)点击 删除成员 按钮， 弹出框，点击 确定， 返回 搜索页面 search_page
        # //*[@text="删除成员"]
        # //*[@text="确定"]
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        from appiumWeChatHomework.page.search_page import SearchPage
        return SearchPage(self._driver)
