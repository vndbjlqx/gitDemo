# 安装 appium server ：$ E:\Program Files\nodejs\node_global\appium_server>npm install --prefix ./ appium

# 启动selenium server 作为 hub 注意：-role hub
# $ java -jar selenium-server-standalone-3.141.59.jar -role hub

# 启动appium 作为 node 注意：-role node
# $ appium --session-override -a 127.0.0.1 -p 4732 --nodeconfig appium_node01.json

# 配置文件启动node，可以启动多个node
# $ appium -a 127.0.0.1 -p 4732 --nodeconfig appium_node01.json
# $ appium -a 127.0.0.1 -p 5732 --nodeconfig appium_node02.json

# $ adb connect 127.0.0.1:7555
# $ adb devices

# $ set udid=127.0.0.1:7555 pytest test_appium_se_grid.py

# --session-override 允许 session 覆盖（如有冲突）
# -a 指定监听的 ip 地址，默认都是127.0.0.1
# -p 指定监听的端口
# --bootstrap-port （仅 Android）设备跟 Appium 通信的端口 这个其实没用了
# --webdriveragent-port 指定ios设备的wda端口
# -U 指定哪台设备，udid
# --local-timezone 时间戳使用本地时区
# --log-timestamp 在终端输出中显示时间戳
# --command-timeout 600  已经弃用了，Desired capabilities
# appium --session-override -a 127.0.0.1 -p 4725  -bp 4726 --udid {your_udid} --command-timeout 600 --webdriveragent-port 8600

import os
from time import sleep
from appium import webdriver


class TestAppiumSeGrid:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"  # 指定操作系统 'Android'
        desired_caps['platformVersion'] = "6.0.1"  # 指定设备版本 '6.0.1'
        # desired_caps['deviceName'] = _deviceName  # 指定设备名称 '127.0.0.1:7555'  $ adb devices
        desired_caps['appPackage'] = "com.xueqiu.android"  # 指定要访问的app，$ adb logcat |grep -i displayed
        desired_caps['appActivity'] = "com.xueqiu.android.common.MainActivity"  # 指定要访问的app的页面，$ adb logcat |grep -i displayed
        # desired_caps['udid'] = os.getenv("udid", None)
        desired_caps['udid'] = "127.0.0.1:7555"
        desired_caps['autoGrantPermission'] = True
        desired_caps['noReset'] = "true"  # 每次不重置应用设置
        desired_caps['skipDeviceInitialization'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'  # 设置中文输入编码
        desired_caps['resetKeyBoard'] = 'true'  # 设置中文输入编码
        desired_caps['appWaitDuration'] = 30000

        self._driver = webdriver.Remote('http://192.168.1.10:4444/wd/hub', desired_caps)  # 指向selenium grid hub
        self._driver.implicitly_wait(5)

    def teardown(self):
        self._driver.quit()

    def test_appium_node(self):
        print("test searching function")
        self._driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self._driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(5)
