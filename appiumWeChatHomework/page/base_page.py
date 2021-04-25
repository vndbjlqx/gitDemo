import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "image_cancel")]  # 查找元素时的黑名单，例如：弹出层
    _error_cont = 0
    _error_max = 5
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find_elements(self, by, locator=None):
        try:
            elements = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_elements(by, locator)
            return elements
        except StaleElementReferenceException as e:
            return []

    def find(self, by, locator=None):
        try:
            # 兼容传过来两个参数，或者一个元祖的形式。
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_cont = 0
            return element
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                elements[0].click()
                return self.find(by, locator)
            # 如果 black_list 没有引起异常的元素，则抛出异常
            raise e

    def scroll_find(self, text):
        swipe_cmd = f"""
                    new UiScrollable(new UiSelector().scrollable(true).instance(0)).
                    scrollIntoView(new UiSelector().text("{text}"));
        """
        return self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, swipe_cmd)

    def swipe_find(self, by, locator=None):
        size = self._driver.get_window_size()
        width = size['width']
        height = size['height']

        startx = width/2
        starty = height * 0.8
        endx = startx
        endy = height * 0.3  # 从下向上滑动
        duration = 2000

        try:
            # 兼容传过来两个参数，或者一个元祖的形式。
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_cont = 0
            return element
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            self._driver.swipe(startx, starty, endx, endy, duration)
            return self.swipe_find(by, locator)

    def send(self, value, by, locator=None):
        element = self.find(by, locator)
        element.clear()
        element.send_keys(value)

    def steps(self, path, func_name):
        with open(path, encoding="utf-8") as f:
            # 指定steps 是 list 类型，且list里面的元素是dict类型
            steps: list[dict] = yaml.safe_load(f)[func_name]
            for step in steps:
                if "by" in step.keys():
                    if "by_value" in step.keys():
                        # 当需要按值点击时：{value}
                        content: str = step["locator"]
                        key: str = step["by_value"]
                        content = content.replace("{%s}" % key, self._params[key])
                        element = self.find(step["by"], content)
                    else:
                        element = self.find(step["by"], step["locator"])
                if "by_scroll" in step.keys():
                    element = self.scroll_find(step["text"])
                if "by_swipe" in step.keys():
                    element = self.swipe_find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        # {value}
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        element.send_keys(content) # 这个 element 已经经过自定义 find 的处理了。
                        # self.send(content, step["by"], step["locator"])
                if "bys" in step.keys():
                    elements = self.find_elements(step["bys"], step["locator"])
                    return elements
