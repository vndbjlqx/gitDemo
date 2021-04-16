from time import sleep

from selenium.webdriver.common.by import By

from seleniumWebDriverHomework.pageObject.base_page import BasePage
from seleniumWebDriverHomework.pageObject.contact_page import ContactPage


class BatchContact(BasePage):

    __upload_file_btn = (By.ID, "js_upload_file_input")
    __sure_upload_btn = (By.ID, "submit_csv")
    __reload_contact = (By.ID, "reloadContact")

    def batch_contact_by_file(self, filePath):
        sleep(3)
        self.send_keys(BatchContact.__upload_file_btn, filePath)
        sleep(2)
        #点击 确认导入 按钮
        self.click(BatchContact.__sure_upload_btn)
        sleep(3)
        #点击 前往查看 按钮
        self.click(BatchContact.__reload_contact)
        sleep(2)
        #返回 通讯录 页面
        return ContactPage(self._driver)

    def goto_contact_page(self):
        return ContactPage(self._driver)