import yaml
from appium import webdriver

from appiumWeChatHomework.page.base_page import BasePage
from appiumWeChatHomework.page.main_page import MainPage


class AppPage(BasePage):
    __env_data_path = "../testData/testEnvData/testEnvData.yml"

    def startApp(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"

        with open(self.__env_data_path) as f:
            envInfo = yaml.safe_load(f)

        targetEnv = envInfo["envInfo"]["targetEnv"]
        _platformName = envInfo["envInfo"][targetEnv]["platformName"]
        _platformVersion = envInfo["envInfo"][targetEnv]["platformVersion"]
        _deviceName = envInfo["envInfo"][targetEnv]["deviceName"]

        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = _platformName         # 指定操作系统 'Android'
            desired_caps['platformVersion'] = _platformVersion   # 指定设备版本 '6.0.1'
            desired_caps['deviceName'] = _deviceName       # 指定设备名称 '127.0.0.1:7555'  $ adb devices
            desired_caps['appPackage'] = _package               # 指定要访问的app，$ adb logcat |grep -i displayed
            desired_caps['appActivity'] = _activity             # 指定要访问的app的页面，$ adb logcat |grep -i displayed
            desired_caps['autoGrantPermission'] = True
            desired_caps['noReset'] = "true"                    # 每次不重置应用设置
            desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['dontStopAppOnReset'] = 'true'
            desired_caps['unicodeKeyBoard'] = 'true'            # 设置中文输入编码
            desired_caps['resetKeyBoard'] = 'true'              # 设置中文输入编码
            desired_caps['appWaitDuration'] = 30000

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package, _activity)

        return self

    def stopApp(self):
        self._driver.quit()

    def main(self):
        return MainPage(self._driver)

