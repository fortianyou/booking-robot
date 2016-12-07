# -*- coding: utf-8 -*-

# 工具类
class Utils(object):

	def __init__(self):
		pass

	# 日志工具方法
	@staticmethod
	def log(typ, msg):
		print "[%s] %s" % (str(typ), str(msg))
		return

	# dict转str
	@staticmethod
	def dict2str(data):
		ans = ''
		for key in data:
			if 0 != len(ans):
				ans += '&'
			ans += str(key) + '=' + str(data[key])
		return ans