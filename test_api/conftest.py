"""
======================
@author:zhuxuanru
@time:2023/7/17 21:41
@email:1435069766@qq.com
======================
"""
import pytest
from common.get_yaml import GetYaml
import os
import sys
from test_api.common.log import Log

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
log = Log()


# 请空all.yaml文件，以便之后写入参数，保持接口关联性
@pytest.fixture(scope="class")
def clear_yamlFile():
	GetYaml("all.yaml").clear_yaml()


@pytest.fixture(scope="class")
def log_main():
	log.info_log("=============测试开始=============")
	yield
	log.info_log("=============测试结束=============")

# @pytest.fixture(scope="function")
# def del_data():
# 	DbOperation().exe_data("delete from user_login where username = '123'")
#
#
# @pytest.fixture(scope="function")
# def get_username():
# 	return DbOperation().query_data("select username,password from user_login order by creat_time desc limit 1")
