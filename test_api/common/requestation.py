"""
======================
@author:zhuxuanru
@time:2023/10/17 14:31
@email:1435069766@qq.com
======================
"""
import requests
from test_api.common.getConfig import GetConfig
from test_api.common.log import Log

path = GetConfig().get_url("test")


class RequestUtil:
	session = requests.session()
	streamLog = Log().creatStreamHandle()
	fileLog = Log().creatFileHandle()

	def all_request(self, url, methods, headers=None, params=None, request_data=None):
		if methods.upper() == "GET":
			try:
				response = self.session.get(url, headers, params)
				self.streamLog.info(f"请求成功,请求地址为{url},请求参数为{params},响应为{response.json()}")
				return response
			except Exception as e:
				self.streamLog.error(f"请求失败,{e}")
		elif methods.upper() == "POST":
			try:
				if headers['Content-Type'] == "application/json":
					response = self.session.post(url=url, json=request_data)
				else:
					response = self.session.post(url=url, data=request_data)
				self.streamLog.info(f"请求成功,请求地址为{url},请求参数为{request_data},响应为{response.json()}")
				return response
			except Exception as e:
				self.streamLog.error(f"请求失败,{e}")
