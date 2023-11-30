"""
======================
@author:zhuxuanru
@time:2023/7/18 20:27
@email:1435069766@qq.com
======================
"""
import yaml
import os
from string import Template
from test_api.common.log import Log


class GetYaml:
	def __init__(self, yaml_name):
		yaml.warnings({'YAMLLoadWarning': False})
		self.yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"test_data/{yaml_name}")
		self.getYamlLog = Log()

	# 读取主流程用例
	def read_main_yaml(self, link=False, **kwargs):
		with open(self.yaml_path, mode="r", encoding='utf-8') as content:
			load_content = yaml.safe_load(content)
			# 接口关联标志，如果为true则直接返回yaml文件内容
			if link:
				self.getYamlLog.info_log(f"-------接口关联,获取all.yaml文件的关联参数{load_content}-------")
				return load_content
			else:
				# 如果kwargs为true，替换成yaml文件里的占位符$
				if kwargs:
					self.getYamlLog.info_log(f"--------替换动态参数--------")
					self.getYamlLog.info_log(f"替换参数为{kwargs}")
					return yaml.safe_load(Template(str(load_content[0])).safe_substitute(kwargs))
				else:
					return load_content[0]

	# 读取单条测试用例各场景
	def read_yaml(self, testcase_name, **kwargs):
		with open(self.yaml_path, mode="r", encoding='utf-8') as content:
			load_content = yaml.safe_load(content)
			for num in range(len(load_content)):
				# 判断测试用例名称是否在yaml文件里
				if testcase_name in load_content[num].keys():
					if kwargs:
						return yaml.safe_load(Template(str(load_content[num][testcase_name])).safe_substitute(kwargs))
					else:
						return load_content[num][testcase_name]
			else:
				return "该测试用例不存在"

	# 写入
	def write_yaml(self, detail):
		with open(self.yaml_path, mode="a", encoding='utf-8') as content:
			yaml.dump(detail, content, default_flow_style=False)

	# 清空
	def clear_yaml(self):
		with open(self.yaml_path, mode="w", encoding='utf-8') as content:
			content.truncate()


# print(GetYaml("xiaodi_home.yaml").read_main_yaml())
