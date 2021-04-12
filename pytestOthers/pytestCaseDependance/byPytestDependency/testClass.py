import pytest

"""
一个模块中有多个class，或重名case，或引入，可以使用类名::用例的方式类依赖
单个类中，使用之前testBasic.py，testName.py中演示的方法也是可以的。
"""

class TestClass(object):

    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        pass


class TestClassNamed(object):

    @pytest.mark.dependency(name="a")
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency(name="b")
    def test_b(self):
        pass

    @pytest.mark.dependency(name="c", depends=["a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(name="d", depends=["b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(name="e", depends=["b", "c"])
    def test_e(self):
        pass