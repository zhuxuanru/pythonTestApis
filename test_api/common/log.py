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
import colorlog

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
localTime = time.strftime("%Y%m%d")


class Log:
	def __init__(self):
		self.logger = logging.getLogger("日志输出")
		self.logger.setLevel(logging.INFO)
		# 设置日志格式和颜色
		self.log_format = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s]-%(levelname)s:%(message)s', log_colors={
			'DEBUG': 'cyan',
			'INFO': 'green',
			'WARNING': 'yellow',
			'ERROR': 'red',
			'CRITICAL': 'red,bg_white',
		})
		# 判断是否有handles，如果有则不会再次添加，防止造成重复打印日志的情况。如果没有则去添加
		if not self.logger.handlers:
			# 设置文件日志的路径名称
			self.fileHandle = logging.FileHandler(filename=log_path + f'/{localTime}.log', mode='a', encoding='UTF-8')
			# 设置文件日志的格式
			self.fileHandle.setFormatter(self.log_format)
			# 将文件日志添加处理器
			self.logger.addHandler(self.fileHandle)
			###############################################
			# 设置控制台日志
			self.streamHandle = logging.StreamHandler()
			# 设置控制台日志的格式
			self.streamHandle.setFormatter(self.log_format)
			# 将控制台日志添加处理器
			self.logger.addHandler(self.streamHandle)

	def info_log(self, message):
		self.logger.info(message)

	def debug_log(self, message):
		self.logger.debug(message)

	def warning_log(self, message):
		self.logger.warning(message)

	def error_log(self, message):
		self.logger.error(message)
