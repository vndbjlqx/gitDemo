from typing import List

def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        # item.name 用例的名字中中文的转码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # item.nodeid 用例的路径中中文的转码
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')