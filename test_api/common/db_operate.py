"""
======================
@author:zhuxuanru
@time:2023/7/17 12:09
@email:1435069766@qq.com
======================
"""

# 导入pymysql
import logging
import pymysql
from test_api.common.get_config import GetConfig


class DbOperation:
	def __init__(self):
		# 链接数据库，查询的结果以字典的形式返回
		self.connect = pymysql.connect(**GetConfig().get_database(), cursorclass=pymysql.cursors.DictCursor)
		# 创建游标
		self.cursor = self.connect.cursor()

	# 查询一条符合条件的数据
	def query_data(self, sql):
		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchone()
			return result
		except pymysql.Error as error:
			logging.error(error)

	# 执行sql
	def exe_data(self, sql):
		try:
			self.cursor.execute(sql)
			self.connect.commit()
		except pymysql.Error as error:
			logging.error(error)

	# 关闭链接和数据库
	def __del__(self):
		self.cursor.close()
		self.connect.close()
