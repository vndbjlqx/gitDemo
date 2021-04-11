"""
注意：我在calculator.py文件中定义的类是Calculator，名字大小写不一样
    import calculator    #导入模块
    calc = calculator.Calculator() #使用模块中的类
    或
    from calculator import Calculator #从模块中导入类
    calc = Calculator() #使用类实例对象

    @pytest.fixture 设置一个测试桩，可以设置使用范围，function为默认范围，需要写入每个func
    自动运行相当于隐式调用。应该是用于初始化一些环境信息。
    如果scope=module 级别，不管在几个func中调用，都只会在该module中执行一次。
    fixture 的yield相当于中间返回，等调用程序执行完成后，再返回执行后面的语句。
"""
import allure
import pytest
import yaml


# pip install pyyaml
def get_datas():
    with open("./testData/data.yml") as f:
        datas = yaml.safe_load(f)
    return datas


@allure.feature("计算器测试")
class TestCalc:

    """
    使用@pytest.mark.parametrize()初始化测试数据之后，func的参数不能有初始值，例如：a=1
    @pytest.mark.parametrize("a,b,exp", [(1, 1, 2), (10, 20, 30), (9, 12, 21)])
    @pytest.mark.parametrize("a,b,exp", yaml.safe_load(open("./testData/data.yml")))
    """
    @pytest.mark.parametrize("a,b,exp", get_datas()['add_int']['datas'])
    @allure.story("整数加法测试")
    def test_add_int(self, calc, a, b, exp):
        with allure.step("进行整数加法"):
            assert calc.add(a, b) == exp

    @pytest.mark.parametrize("a,b,exp", get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    @allure.story("浮点数加法测试")
    def test_add_float(self, calc, a, b, exp):
        with allure.step("进行浮点数加法"):
            assert calc.add(a, b) == exp

    @pytest.mark.parametrize("a,b,exp", get_datas()['div_int']['datas'])
    @allure.story("整数除法测试")
    def test_div_int(self, calc, a, b, exp):
        with allure.step("进行整数除法"):
            assert calc.div(a, b) == exp

    @pytest.mark.parametrize("a,b,exp", get_datas()['div_zero']['datas'])
    @allure.story("被除数为0的除法测试")
    def test_div_zero(self, calc, a, b, exp):
        with allure.step("进行被除数为0的除法"):
            with pytest.raises(ZeroDivisionError):
                calc.div(a, b)

    @pytest.mark.parametrize("a,b,exp", get_datas()['div_round']['datas'])
    @allure.story("循环小数保留2位测试")
    def test_div_round(self, calc, a, b, exp):
        with allure.step("进行循环小数保留2"):
            assert exp == round(calc.div(a, b), 2)

    @pytest.mark.parametrize("a,b,exp", get_datas()['div_float']['datas'])
    @allure.story("浮点数除法测试")
    def test_div_float(self, calc, a, b, exp):
        with allure.step("进行浮点数除法"):
            assert calc.div(a, b) == exp

    @allure.story("失败测试")
    def test_case_false(self):
        with allure.step("失败测试"):
           assert 1==2

    @pytest.mark.skipif(1==1, reason="测试条件未满足")
    @allure.story("忽略测试")
    def test_case_skip(self):
            with allure.step("忽略测试"):
               assert 1==2

