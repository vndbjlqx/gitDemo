import yaml


class Utils:

    def readYmlFile(self, filename, casename):
        basic_test_data_path = f"../testData/testCaseData/{filename}.yml"
        with open(basic_test_data_path, encoding="utf-8") as f:
            test_data = yaml.safe_load(f)
        return test_data[casename]["datas"]
