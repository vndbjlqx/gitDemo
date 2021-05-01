# 需要下载selenium-server-standalong-3.141.59.jar
# https://www.selenium.dev/downloads/
# 把 JDK / chrome driver 或其他浏览器driver 配置到环境变量

# 设置节点文件 node.json
# 用例参考：https://github.com/SeleniumHQ/selenium/blob/selenium-3.141.59/java/server/src/org/openqa/grid/common/defaults/DefaultNodeWebDriver.json
# https://github.com/SeleniumHQ/selenium/wiki/Grid2

# 启动selenium server 作为 hub 注意：-role hub
# $ java -jar selenium-server-standalone-3.141.59.jar -role hub

# 启动selenium server 作为 node 注意：-role node
# $ java -jar selenium-server-standalone-3.141.59.jar -role node [-port 5677]

# 配置文件启动node，可以启动多个node
# $ java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node.json
# $ java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node.json
# $ java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node.json

# 测试工具设置
# setting - tools - python integration tools - 设置test用pytest
import logging
import threading


from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

logging.basicConfig(level=logging.INFO)

class TestGrid:
    def test_grid(self):
        hub_url = "http://127.0.0.1:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1,5):
            driver =Remote(command_executor=hub_url,desired_capabilities=capability)
            driver.get("https://www.baidu.com/")

    def my_case(self):
        logging.info("begin calling my_case")
        hub_url = "http://127.0.0.1:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        driver = Remote(command_executor=hub_url, desired_capabilities=capability)
        driver.get("https://www.baidu.com/")
        logging.info("end calling my_case")

    def test_grid_in_mutithread(self):
        # "maxInstances": 5, 每个node里面，最多启动 5 个指定的浏览器，这是一个浏览器的字典设置参数。关心的是每种浏览器最多启动几个。
        # "maxSession": 5,  The maximum number of browsers that can run in parallel on the node. 关心的是在node上最多起动几个浏览器。
        logging.info("begin test_grid_in_mutithread")
        threads = []
        nloops = range(5)
        for i in nloops:
            #这里可以指定每个线程做不同的case
            t = threading.Thread(target=self.my_case)
            threads.append(t)
        for i in nloops:
            threads[i].start()
        for i in nloops:
            threads[i].join()

        logging.info("end test_grid_in_mutithread")















