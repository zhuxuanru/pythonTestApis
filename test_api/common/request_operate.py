"""
======================
@author:zhuxuanru
@time:2023/10/17 14:31
@email:1435069766@qq.com
======================
"""
import requests
from test_api.common.get_config import GetConfig
from test_api.common.log import Log

path = GetConfig().get_url("test")


class RequestUtil:
	session = requests.session()
	requestLog = Log()

	def all_request(self, url, methods, headers, params=None, request_data=None):
		if methods.upper() == "GET":
			try:
				self.request_log(url, methods, headers, params)
				response = self.session.get(url=url, headers=headers, params=params)
				self.response_log(response.json())
				return response
			except Exception as e:
				self.requestLog.error_log(f"请求失败,{e}")
		elif methods.upper() == "POST":
			try:
				self.request_log(url, methods, headers, request_data)
				if headers['Content-Type'] == "application/json":
					response = self.session.post(url=url, json=request_data)
					self.response_log(response.json())
				else:
					response = self.session.post(url=url, data=request_data)
					self.response_log(response.json())
				return response
			except Exception as e:
				self.requestLog.error_log(f"请求失败,{e}")

	def request_log(self, url, method, headers, data):
		self.requestLog.info_log(f"请求接口地址--------------->{url}")
		self.requestLog.info_log(f"请求接口的请求方式--------------->{method}")
		self.requestLog.info_log(f"请求接口的请求头--------------->{headers}")
		self.requestLog.info_log(f"请求接口的请求参数--------------->{data}")

	def response_log(self, response_json):
		self.requestLog.info_log(f"请求接口的响应--------------->{response_json}")
