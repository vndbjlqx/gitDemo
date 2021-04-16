from selenium.webdriver.common.by import By

from seleniumWebDriverHomework.pageObject.base_page import BasePage


class AddMember(BasePage):

    __user_name = (By.ID, "username")
    __member_acc_id = (By.ID, "memberAdd_acctid")
    __member_phone = (By.ID, "memberAdd_phone")
    __save_btn = (By.XPATH, ".//*[contains(@class,'js_btn_save')][1]")

    def add_member(self, member):
       self.send_keys(AddMember.__user_name, member["username"])
       self.send_keys(AddMember.__member_acc_id, member["accid"])
       self.send_keys(AddMember.__member_phone, member["phone"])
       self.click(AddMember.__save_btn)

       from seleniumWebDriverHomework.pageObject.contact_page import ContactPage
       return ContactPage(self._driver)


