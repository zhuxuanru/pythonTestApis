"""
======================
@author:zhuxuanru
@time:2023/11/10 19:43
@email:1435069766@qq.com
======================
"""
import logging
import os
import time

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
localTime = time.strftime("%Y%m%d")


class Log:
	def __init__(self):
		self.logger = logging.getLogger("日志输出")
		self.logger.setLevel(logging.DEBUG)
		self.log_format = logging.Formatter('[%(asctime)s]-%(levelname)s:%(message)s')

	def creatFileHandle(self):
		if not self.logger.handlers:
			# 设置文件的路径名称，写入方式
			fileHandle = logging.FileHandler(filename=log_path + f'/{localTime}.log', mode='a', encoding='UTF-8')
			# fileHandle.setLevel(logging.DEBUG)
			# 设置文件日志的格式
			fileHandle.setFormatter(self.log_format)
			# 添加文件处理器
			self.logger.addHandler(fileHandle)
			return self.logger
		else:
			return self.logger

	def creatStreamHandle(self):
		# 判断是否有handles，如果有则不会再次添加，防止造成重复打印日志的情况。如果没有则去添加
		if not self.logger.handlers:
			streamHandle = logging.StreamHandler()
			streamHandle.setFormatter(self.log_format)
			self.logger.addHandler(streamHandle)
			return self.logger
		else:
			return self.logger

