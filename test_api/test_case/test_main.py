"""
======================
@author:zhuxuanru
@time:2023/11/5 16:15
@email:1435069766@qq.com
======================
一级用例，登录查询goods
"""
from string import Template
import allure
import pytest
from test_api.common.request_operate import RequestUtil
from test_api.common.get_yaml import GetYaml
from test_api.common.get_config import GetConfig
from test_api.common.generate_data import GeneratedData
from test_api.common.assert_data import Check_data
from test_api.common.crypt_data import MD5_encode

path = GetConfig().get_url("test")
getYamlLogin = GetYaml("login.yaml")
getYamlGoods = GetYaml("goods.yaml")
getYamlForm = GetYaml("form.yaml")
getYamlAll = GetYaml("all.yaml")
request = RequestUtil()
check = Check_data()
# md5加密测试接口
# username = MD5_encode("admin")
# password = MD5_encode("admin123")
# 随机生成账号密码
username = GeneratedData().generatedName()
password = GeneratedData().generatedRandomNumber(8)


@allure.feature("登录查询form表单")
class Test_main:

	@allure.story("登录")
	# 将该方法打上login标签
	@pytest.mark.login
	# 失败重新执行2次
	@pytest.mark.flaky(reruns=2)
	# 执行顺序（第一个执行）
	@pytest.mark.run(order=1)
	# 参数化，请求参数，方法，地址从login.yaml文件里取
	@pytest.mark.parametrize("testcase_list", [getYamlLogin.read_main_yaml(username=username, password=password)])
	def test_login(self, clear_yamlFile, testcase_list):
		testcase = testcase_list["test_login_01"]
		url = path + testcase["url"]
		response = request.all_request(url, testcase["method"], testcase['headers'], request_data=testcase["data"])
		# 多重断言assume，前面断言失败后面也会执行
		pytest.assume(response.status_code == 200)
		check.key_check(response.json(), testcase["valid"])
		check.value_check(response.json(), testcase["valid"])
		# 将该接口返回写入到all.yaml文件中
		GetYaml("all.yaml").write_yaml({"uid": response.json()["uid"]})

	@allure.story("查询goods")
	@pytest.mark.run(order=2)
	@pytest.mark.queryGoods
	@pytest.mark.parametrize("testcase", [getYamlGoods.read_main_yaml()])
	def test_queryGoods(self, testcase):
		url = path + testcase["url"]
		# 获取上一个接口的返回参数用于该接口的请求
		data = Template(str(testcase["data"])).safe_substitute(getYamlAll.read_main_yaml(link=True))
		response = request.all_request(url, testcase["method"], testcase['headers'], request_data=eval(data))
		pytest.assume(response.status_code == 200)
		check.key_check(response.json(), testcase["valid"])
		check.value_check(response.json(), testcase["valid"])

	@allure.story("查询form表单")
	@pytest.mark.run(order=3)
	@pytest.mark.formData
	@pytest.mark.parametrize("testcase", [getYamlForm.read_main_yaml(name=username)])
	def test_formData(self, testcase):
		url = path + testcase["url"]
		request_data = testcase["data"]
		response = request.all_request(url, testcase["method"], testcase['headers'], request_data=request_data)
		pytest.assume(response.status_code == 200)
		check.key_check(response.json(), testcase["valid"])
		check.value_check(response.json(), testcase["valid"])

