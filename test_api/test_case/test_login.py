"""
======================
@author:zhuxuanru
@time:2023/11/14 17:37
@email:1435069766@qq.com
======================
针对登录各种场景的用例
"""
import allure
import pytest

from test_api.common.generate_data import GeneratedData
from test_api.common.get_yaml import GetYaml
from test_api.common.get_config import GetConfig
from test_api.common.request_operate import RequestUtil

getYamlLogin = GetYaml("login.yaml")
path = GetConfig().get_url("test")
request = RequestUtil()

username = GeneratedData().generatedName()
password = GeneratedData().generatedRandomNumber(8)


@allure.feature("登录接口测试用例")
class Test_login:

	@allure.story("登录成功")
	@pytest.mark.parametrize("testcase", [GetYaml("login.yaml").read_yaml(testcase_name="test_login_01",
																		username=username, password=password)])
	def test_login_01(self, testcase):
		url = path + testcase["url"]
		response = request.all_request(url, testcase["method"], testcase["headers"], request_data=testcase["data"])
		pytest.assume(response.status_code == 200)
		pytest.assume(response.json()["msg"] == testcase["valid"])

	@allure.story("未传用户名,登录失败")
	@pytest.mark.parametrize("testcase", [GetYaml("login.yaml").read_yaml(testcase_name="test_login_02", password=password)])
	def test_login_02(self, testcase):
		url = path + testcase["url"]
		response = request.all_request(url, testcase["method"], testcase["headers"], request_data=testcase["data"])
		pytest.assume(response.status_code == 200)
		pytest.assume(response.json()["msg"] == testcase["valid"])
