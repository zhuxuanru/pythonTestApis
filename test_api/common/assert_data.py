"""
======================
@author:zhuxuanru
@time:2023/11/15 15:55
@email:1435069766@qq.com
======================
"""
from test_api.common.log import Log


class Check_data:
	def __init__(self):
		self.check_data_log = Log()
		self.check_list = []

	# 检查接口json格式的返回key，是否与预期结果返回key相等
	def key_check(self, really_key, except_key):
		if len(really_key) != len(except_key):
			self.check_list.append(False)
			Log().error_log("------预期结果和实际结果字段数量不一致------")
		else:
			for key in except_key.keys():
				if key in really_key:
					self.check_list.append(True)
				else:
					self.check_list.append(False)
					Log().error_log(f"------预期结果中不存在实际结果中的{key}字段------")

		if False in self.check_list:
			Log().error_log(f"断言方式[json-key]------>预期结果{really_key},实际结果{except_key},断言失败")
		else:
			Log().info_log(f"断言方式[json-key]------->预期结果{really_key},实际结果{except_key},断言通过")

	def value_check(self, really_value, except_value):
		# except_value_dict = eval(str(except_value))
		for key, value in really_value.items():
			if value in except_value.values():
				self.check_list.append(True)
			else:
				self.check_list.append(False)
				Log().error_log(f"------实际结果中{key}字段的{value}值和预期结果不一致------")

		if False in self.check_list:
			Log().error_log(f"断言方式[json-value]------>预期结果{really_value},实际结果{except_value},断言失败")
		else:
			Log().info_log(f"断言方式[json-value]------>预期结果{really_value},实际结果{except_value},断言通过")

