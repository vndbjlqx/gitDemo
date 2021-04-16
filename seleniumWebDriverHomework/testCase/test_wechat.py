import pytest

from seleniumWebDriverHomework.testCase.base_case import BaseCase
from seleniumWebDriverHomework.utils.utils import Utils


class TestWeChat(BaseCase):

    """
        1. 在 主页面 点击 添加成员 按钮，跳转到 添加成员页面
        2. 在 添加成员 页面 输入 成员信息，保存， 跳转到 通讯录 页面
        3. 在 通讯录页面 获得 成员列表， 判断 新成员在列表中
    """
    @pytest.mark.skip
    def test_add_member(self):
        # member = {"username": "Alice", "accid": "11019876", "phone": "13657609847"}
        member = self.test_data["test_add_member"]["datas"]["member"]
        contact_list_names = self.main.goto_add_member_page().add_member(member).get_contact_list()
        assert member["username"] in contact_list_names

    """
        添加部门
        1.主页面，点击顶部 通讯录 链接，返回 通讯录页面
        2.在通讯录页面，点击 加号，返回 添加部门页面
        3.填写部门信息，保持，返回 通讯录页面
        4.在通讯录页面检查添加的新部门是否成功
    """
    @pytest.mark.parametrize("depart_name, parent_depart_name",
                             Utils().readYmlFile("TestWeChat", "test_add_department"))
    def test_add_department(self, depart_name, parent_depart_name):
        # depart_name = "abc001"
        # parent_depart_name = "刘群星企业微信"
        depart_list_names = self.main\
            .goto_contact_page()\
            .goto_add_department_page()\
            .add_department(depart_name, parent_depart_name)\
            .get_department_list()
        assert depart_name in depart_list_names

    """
        导入通讯录
        1. 主页面 点击 下面的 导入通讯录， 返回 批量导入页面
        2. 批量导入页面， 点击 上传，输入文件路径(windows文件上传)，点击 确认导入， 点击 前往查看
        3. 通讯录页面，检查人员列表
        4. 通讯录页面，检查部门列表生成
    """
    @pytest.mark.skip
    @pytest.mark.parametrize("file_path, expect_names",
                             Utils().readYmlFile("TestWeChat", "test_batch_add_contact_by_file"))
    def test_batch_add_contact_by_file(self, file_path, expect_names):
        # file_path = "E:\PycharmProjects\gitDemo\seleniumWebDriverHomework\\testData\\batchEmp.xlsx"
        # exp_contact_names = ["张三", "王五"]
        file_path_val = file_path["file_path"]
        exp_contact_names_vals = expect_names["expect_names"]
        contact_list_names = self.main\
            .goto_batch_contact_page()\
            .batch_contact_by_file(file_path_val)\
            .get_contact_list()

        for name in exp_contact_names_vals:
            if not (name in contact_list_names):
                assert False
                return

        assert True
