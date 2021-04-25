import pytest

from appiumWeChatHomework.testcase.base_case import BaseCase
from appiumWeChatHomework.utils.utils import Utils


class TestWeChatEnterpriseApp(BaseCase):

    def setup(self):
        pass

    def teardown(self):
        # 返回主页面
        #self.app.main().goto_msg_page()
        pass

    # @pytest.mark.skip
    # @pytest.mark.parametrize("name, phone", [("马小西", "13810000215")])
    @pytest.mark.parametrize("name, phone",
                             Utils().readYmlFile("TestWeChatEnterpriseApp", "test_add_friend"))
    def test_add_friend(self, name, phone):
        contact_list = self.app.main()\
            .goto_contact_list_page()\
            .goto_add_friend_page()\
            .goto_manual_add_friend_page()\
            .input_friend_info(name, phone)\
            .save()\
            .back()\
            .get_contact_list()

        assert name in contact_list

   # @pytest.mark.parametrize("name", ["李小西"])
   # @pytest.mark.skip
    @pytest.mark.parametrize("name",
                             Utils().readYmlFile("TestWeChatEnterpriseApp", "test_delete_friend"))
    def test_delete_friend(self, name):
        print("abc")
        searchPageObj = self.app.main()\
                    .goto_contact_list_page()\
                    .search()\
                    .search_and_select_person_by_name(name)\
                    .edit_person_info().edit_member()\
                    .delete_person()\
                    .search_person_result_list()

        searchPageObj.back_to_contact_list_page()
        person_list = searchPageObj.search_person_list
        assert len(person_list) == 0
