"""
======================
@author:zhuxuanru
@time:2023/7/17 21:57
@email:1435069766@qq.com
======================
"""
import configparser
import os

# 需要读取配置文件的路径
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configs/config.ini")


class GetConfig:
	def __init__(self):
		# 创建对象
		self.cf = configparser.ConfigParser()
		# 读取该配置文件
		self.cf.read(config_path)

	# 获取数据库配置信息
	def get_database(self):
		database_dict = {}
		# f.items(section="database")获取节点database下的配置信息
		for key, value in self.cf.items(section="database"):
			if key == "port":
				database_dict[key] = int(value)
			else:
				database_dict[key] = value
		return database_dict

	# 获取测试环境地址
	def get_url(self, name):
		return self.cf.get("url", name)

