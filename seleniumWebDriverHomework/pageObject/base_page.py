import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from seleniumWebDriverHomework.utils.factory_webdriver import FactoryWebDriver


class BasePage:
    _base_url = ""
    __env_data_path = "../testData/testEnvData/testEnvData.yml"
    """
    封装页面通用方法，比如driver的实例化
    """
    def __init__(self, base_driver=None):
        """
        :param base_driver: 传入driver 实例对象
        """
        # 如果 base_driver 是初始值None，那么就会实例化driver
        if base_driver is not None:
            self._driver = base_driver
        else:
            with open(BasePage.__env_data_path) as f:
                envInfo = yaml.safe_load(f)

            targetEnv = envInfo["envInfo"]["targetEnv"]
            browser_type =  envInfo["envInfo"]["tar_Browser"]
            self._base_url =  envInfo["envInfo"][targetEnv]["url"]

            self._driver = FactoryWebDriver().create_webdriver(targetEnv, browser_type)
            # if targetEnv == "debug_env":
            #     # 浏览器类型，测试环境类型，对应测试环境的初始url
            #     chrome_arg = webdriver.ChromeOptions()  # 使用浏览器复用模式
            #     chrome_arg.debugger_address = '127.0.0.1:9222'  # 加入调试地址
            #     self._driver = webdriver.Chrome(options=chrome_arg)  # 实例化driver对象
            # else:
            #     if browser_type == "Firefox":
            #         print("# 初始化 Firefox driver")
            #     elif browser_type == "IE":
            #         print("# 初始化 IE driver")
            #     elif browser_type == "Headless":
            #         print("# 初始化 Headless driver")
            #     else:
            #         self._driver = webdriver.Chrome()

            if self._base_url != "":
                self._driver.get(self._base_url)
                # 隐式等待，会在每次find 操作的时候，轮询查找该元素，超时报错
                self._driver.implicitly_wait(3)
            else:
                raise Exception("Exception: base url is empty.")

    def find(self, locator):
        # 解元祖的操作
        def wait(x):
            return len(self._driver.find_elements(*locator)) > 0

        WebDriverWait(self._driver, 5).until(wait)
        return self._driver.find_element(*locator)

    def find_elements(self, locator):
        return self._driver.find_elements(*locator)

    def click(self, locator):
        self.find(locator).click()

    def send_keys(self, locator, msg):
        self.find(locator).send_keys(msg)

    def get_list_texts(self, locator):
        ele_list = self.find_elements(locator)
        text_list = [i.text for i in ele_list]
        # name_list = []
        # for i in ele_list:
        #     name_list.append(i.text)
        # print(name_list)
        return text_list

    def js_click(self, js_cmd):
        el = self._driver.execute_script(f"return {js_cmd}")
        el.click()