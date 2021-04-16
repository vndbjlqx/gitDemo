import yaml

from seleniumWebDriverHomework.pageObject.main_page import MainPage


class BaseCase:
    __basic_test_data_path = "../testData/testCaseData/"

    def setup_class(self):
        print("Running BaseCase::setup_class")
        test_data_path = BaseCase.__basic_test_data_path + self.__name__+".yml"
        with open(test_data_path, encoding="utf-8") as f:
            test_data = yaml.safe_load(f)

        self.main = MainPage()
        self.test_data = test_data

    def teardown_class(self):
        print("Running BaseCase::setup_class")


