"""
======================
@author:zhuxuanru
@time:2023/11/5 16:15
@email:1435069766@qq.com
======================
"""
from string import Template
import allure
import pytest
from test_api.common.requestation import RequestUtil
from test_api.common.getYaml import GetYaml
from test_api.common.getConfig import GetConfig
from test_api.common.cryptData import MD5_encode

path = GetConfig().get_url("test")
# md5加密测试接口
username = MD5_encode("admin")
password = MD5_encode("admin123")


@allure.feature("登录查询form表单")
class Test_login:

	@allure.story("登录")
	# 将该方法打上login标签
	@pytest.mark.login
	# 失败重新执行2次
	@pytest.mark.flaky(reruns=2)
	# 执行顺序（第一个执行）
	@pytest.mark.run(order=1)
	# 参数化，请求参数，方法，地址从login.yaml文件里取
	@pytest.mark.parametrize("testcase", GetYaml("login.yaml").read_yaml(username=username, password=password))
	def test_login(self, clear_yamlFile, testcase):
		url = path + testcase["url"]
		response = RequestUtil().all_request(url=url, methods=testcase["method"], headers=testcase['headers'],
											 request_data=testcase["data"])
		# 多重断言assume，前面断言失败后面也会执行
		pytest.assume(response.status_code == 200)
		pytest.assume(response.json()["msg"] == testcase["msg"])
		# 将该接口返回写入到all.yaml文件中
		GetYaml("all.yaml").write_yaml({"uid": response.json()["uid"]})

	@allure.story("查询goods")
	@pytest.mark.run(order=2)
	@pytest.mark.queryGoods
	@pytest.mark.parametrize("testcase", GetYaml("goods.yaml").read_yaml())
	def test_queryGoods(self, testcase):
		url = path + testcase["url"]
		# 获取上一个接口的返回参数用于该接口的请求
		data = Template(str(testcase["data"])).safe_substitute(GetYaml("all.yaml").read_yaml())
		response = RequestUtil().all_request(url=url, methods=testcase["method"], headers=testcase['headers'],
											 request_data=eval(data))
		pytest.assume(response.status_code == 200)
		pytest.assume(response.json()["msg"] == testcase["msg"])

	@allure.story("查询form表单")
	@pytest.mark.run(order=3)
	@pytest.mark.formData
	@pytest.mark.parametrize("testcase", GetYaml("form.yaml").read_yaml(name=username))
	def test_formData(self, testcase):
		url = path + testcase["url"]
		request_data = testcase["data"]
		response = RequestUtil().all_request(url=url, methods=testcase["method"], headers=testcase['headers'],
											 request_data=request_data)
		pytest.assume(response.status_code == 200)
		pytest.assume(response.json()["msg"] == testcase["valid"]["msg"])
		pytest.assume(response.json()["age"] == testcase["valid"]["age"])

