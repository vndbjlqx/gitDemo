import pytest
from calculator import Calculator
from typing import List

"""
    将fixture的scope设置为class级别，就相当于setupClass，tearDownClass，
    这样做可以减少创建calculator对象的数量。
"""
# @pytest.fixture()
@pytest.fixture(scope="class")
def calc():
    print("........... cal begin..........")
    calc = Calculator()
    #return calc
    yield calc
    print("........... cal end...........")


def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        # item.name 用例的名字中中文的转码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径中中文的转码
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')