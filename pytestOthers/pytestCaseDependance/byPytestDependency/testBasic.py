import pytest
"""
resuts:
test_a
    deliberately fails.
test_b
    succeeds.
test_c
    will be skipped because it depends on test_a.
test_d
    depends on test_b which did succeed. 
    It will be run and succeed as well.
test_e
    depends on test_b and test_c. test_b did succeed, 
    but test_c has been skipped. So this one will also be skipped. 
"""


@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False

#要使后面的用例形成依赖关系，前面的用例必须加这个装饰器
@pytest.mark.dependency()
def test_b():
    pass

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass

@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    pass