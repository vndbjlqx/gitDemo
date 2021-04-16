from time import sleep

from selenium.webdriver.common.by import By

from seleniumWebDriverHomework.pageObject.base_page import BasePage


class AddDepartment(BasePage):

    __depart_name = (By.CSS_SELECTOR, ".inputDlg_item:nth-child(1) input")
    __expand_dep_list = (By.CSS_SELECTOR, ".inputDlg_item:nth-child(3) > a")
    __submit_btn = (By.XPATH, ".//a[@d_ck='submit']")

    def add_department(self, dep_name, parent_dep):
        self.send_keys(AddDepartment.__depart_name, dep_name)
        self.click(AddDepartment.__expand_dep_list)
        loc = f'.//form//li[@role="treeitem"]//a[text()="{parent_dep}"]'
        tup = (By.XPATH, loc)
        self.click(tup)
        self.click(AddDepartment.__submit_btn)
        sleep(3)
        # 使用局部引用，解决循环引用问题
        from seleniumWebDriverHomework.pageObject.contact_page import ContactPage
        return ContactPage(self._driver)
