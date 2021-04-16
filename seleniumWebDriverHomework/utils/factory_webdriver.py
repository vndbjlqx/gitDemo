from selenium import webdriver

class FactoryWebDriver:

    def create_webdriver(self, target_env, browser_type):
        if target_env == "debug_env":
            # 浏览器类型，测试环境类型，对应测试环境的初始url
            chrome_arg = webdriver.ChromeOptions()  # 使用浏览器复用模式
            chrome_arg.debugger_address = '127.0.0.1:9222'  # 加入调试地址
            self._driver = webdriver.Chrome(options=chrome_arg)  # 实例化driver对象
        else:
            if browser_type == "Firefox":
                print("# 初始化 Firefox driver")
            elif browser_type == "IE":
                print("# 初始化 IE driver")
            elif browser_type == "Headless":
                print("# 初始化 Headless driver")
            else:
                self._driver = webdriver.Chrome()

        return self._driver