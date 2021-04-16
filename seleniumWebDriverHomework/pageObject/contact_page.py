from time import sleep

from selenium.webdriver.common.by import By

from seleniumWebDriverHomework.pageObject.add_department import AddDepartment
from seleniumWebDriverHomework.pageObject.add_member import AddMember
from seleniumWebDriverHomework.pageObject.base_page import BasePage


class ContactPage(BasePage):
    __member_colLeft_top_addBtn = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __add_department = (By.CSS_SELECTOR, ".js_create_party")
    __department_list = (By.XPATH, ".//div[@class='member_colLeft_bottom']//a[contains(@class,'jstree-anchor')]")
    __contact_member_list = (By.XPATH, ".//tbody[contains(@class,'js_list')]/tr/td[2]")

    def get_contact_list(self):
        sleep(3)
        return self.get_list_texts(ContactPage.__contact_member_list)

    def get_department_list(self):
        sleep(3)
        return self.get_list_texts(ContactPage.__department_list)

    def goto_add_member_page(self):
        return AddMember(self._driver)

    def goto_add_department_page(self):
        sleep(3)
        self.click(ContactPage.__member_colLeft_top_addBtn)
        self.click(ContactPage.__add_department)
        return AddDepartment(self._driver)
