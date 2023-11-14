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


class GetYaml:
	def __init__(self, yaml_name):
		yaml.warnings({'YAMLLoadWarning': False})
		self.yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"test_data/{yaml_name}")

	# 读取
	def read_yaml(self, **kwargs):
		with open(self.yaml_path, mode="r", encoding='utf-8') as content:
			result = yaml.safe_load(content)
			# 如果kwargs为true，替换成yaml文件里的占位符$
			if kwargs:
				return yaml.safe_load(Template(str(result)).safe_substitute(kwargs))
			else:
				return result

	# 写入
	def write_yaml(self, detail):
		with open(self.yaml_path, mode="a", encoding='utf-8') as content:
			yaml.dump(detail, content, default_flow_style=False)

	# 清空
	def clear_yaml(self):
		with open(self.yaml_path, mode="w", encoding='utf-8') as content:
			content.truncate()

