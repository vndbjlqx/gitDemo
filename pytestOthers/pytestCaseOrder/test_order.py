import pytest

"""
pip install pytest-ordering
pip install pytest-ordering -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

前提：安装pytest-ordering
@pytest.mark.run(order=-3)

orders_map = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
    'sixth': 5,
    'seventh': 6,
    'eighth': 7,
    'last': -1,
    'second_to_last': -2,
    'third_to_last': -3,
    'fourth_to_last': -4,
    'fifth_to_last': -5,
    'sixth_to_last': -6,
    'seventh_to_last': -7,
    'eighth_to_last': -8,
}
"""


class TestPytest(object):

    @pytest.mark.run(order=-3)
    def test_one(self):
        print("test_one")
        pass

    @pytest.mark.run(order=-1)
    def test_two(self):
        print("test_two")
        pass

    @pytest.mark.run(order=1)
    def test_three(self):
        print("test_three")
        pass