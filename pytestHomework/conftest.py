import pytest
from calculator import Calculator


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