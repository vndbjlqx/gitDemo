import sys
from time import sleep

from appium.webdriver import WebElement
from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.person_info_page import PersonInfoPage


class SearchPage(BasePage):
    # 注意这个路径是从调用的位置开始计算的
    file_path = "../page/search_page.yml"

    def search_person(self, name):
        # search_person
        # //*[@text="搜索"]
        self._params["search_person_name"] = name
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return self

    def search_and_select_person_by_name(self, name):
        # 搜索 姓名 ，从列表中选择 用户，转向 个人信息页面 person_info_page
        self._params["search_person_name"] = name
        self.search_person(name)
        sleep(5)
        # //android.widget.TextView[@text="马小男"]
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        return PersonInfoPage(self._driver)

    def search_person_result_list(self):
        # 返回搜索到的结果list
        sleep(5)
        # //android.view.ViewGroup/android.widget.TextView
        elements: list[WebElement] = self.steps(self.file_path, sys._getframe().f_code.co_name)
        person_name = []
        for el in elements:
            person_name.append(el.text)
        self.search_person_list = person_name
        return self

    def back_to_contact_list_page(self):
        # //android.widget.LinearLayout/android.widget.TextView
        self.steps(self.file_path, sys._getframe().f_code.co_name)
        from appiumWeChatHomework.page.contact_list_page import ContactListPage
        return ContactListPage(self._driver)