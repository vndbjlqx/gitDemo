# gitDemo
my git demo repository
update this file for testing.

#使用镜像安装插件
pip install [pyyaml] -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

#总结一些坑
创建包，会有__init__.py文件，说明这是一个module，一般文件夹没有。
你只能从 包 中导入module，类， 所以，出现在 import 语句中的路径下必须有__init__.py
from seleniumWebDriverHomework.pageObject.main_page import MainPage
ModuleNotFoundError: No module named 'seleniumWebDriverHomework'

注意循环引用的问题，只定义去的，不定义回来的。

testcase的类不能有 构造函数 __init__()

上传文件按钮不用click，直接send_keys(文件绝对路径)

处理yml文件读取时的编码设置，否则中文会出问题open(yml_path, encoding="utf-8")

@pytest.mark.parametrize 加载数据，返回数据最好是list类型，方便成组。

调用顺序，@pytest[parametrize数据加载]，setup_xx, [类实例, __init()__], testcase

尝试了在setup_class 方法中加载数据，
- 优点，可以使用self.datas记录数据，在所有case中可用。
       可以使用 self.__name__ 得到当前类名，自动拼装数据文件路径。
- 缺点，无法自动封装参数，多组数据时无法自动运行用例。

尝试了使用fixture定义一个方法级别的桩，
- 缺点，没法自动获得当前调用的 testcase 名称，
       无法自动封装参数，多组数据时无法自动运行用例。
  
尝试了使用@pytest.mark.parametrize初始化数据，
- 优点，可以自动封装参数，多组数据可以自动执行，
- 缺点，需要单独定义Utils类，定义读取数据方法，文件名，testcase名，无法自动获得
