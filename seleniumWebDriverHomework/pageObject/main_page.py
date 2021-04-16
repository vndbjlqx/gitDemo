from selenium.webdriver.common.by import By

from seleniumWebDriverHomework.pageObject.add_member import AddMember
from seleniumWebDriverHomework.pageObject.base_page import BasePage
from seleniumWebDriverHomework.pageObject.contact_page import ContactPage
from seleniumWebDriverHomework.pageObject.batch_contact import BatchContact


class MainPage(BasePage):

    __top_menu_contacts = (By.ID, "menu_contacts")
    __batch_import = (By.XPATH, ".//a[@node-type='import']")
    __add_member = (By.XPATH, ".//a[@node-type='addmember']")

    def goto_add_member_page(self):
        self.click(MainPage.__add_member)
        return AddMember(self._driver)

    #打开通讯录页面
    def goto_contact_page(self):
        self.click(MainPage.__top_menu_contacts)
        return ContactPage(self._driver)

    # 打开导入通讯录
    def goto_batch_contact_page(self):
        self.click(MainPage.__batch_import)
        return BatchContact(self._driver)
