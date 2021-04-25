import yaml

from appiumWeChatHomework.page.app_page import AppPage


class BaseCase:
   # __basic_test_data_path = "../testData/testCaseData/"
    app = AppPage()

    def setup_class(self):
        # 创建 driver
        # 打开app，访问 mainpage
        self.app.startApp()

        # # 读取用例的数据文件
        # test_data_path = BaseCase.__basic_test_data_path + self.__name__ + ".yml"
        # with open(test_data_path, encoding="utf-8") as f:
        #     test_data = yaml.safe_load(f)
        #
        # self.test_data = test_data


    def teardown_class(self):
        # 删除 driver
        # self.app.stopApp()
        pass
