# -*- coding: utf-8 -*-
 
import urllib
import urllib2
import cookielib
import re
import pytesseract
from PIL import Image

import iconfig
from utils import Utils

# 东方时尚驾校
class EasternPioneer(object):

	def __init__(self):
		self.pdata = {
			'AjaxMethod' : 'LOGIN',
			'Account' : '',
			'Pwd' : '',
			'ValidCode' : ''
		}

		self.operate = '' # response对象(不含read)
		self.cj = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		urllib2.install_opener(self.opener)
		
		return

	# 登录
	def login(self, account='', password=''):
		self.pdata['Account'] = account
		self.pdata['Pwd'] = password

		Utils.log("INFO", "登录中 ...")

		Utils.log("INFO", "获取验证码中 ...")
		self._get_icode_img()

		Utils.log("INFO", "识别验证码中 ...")
		self._identify_icode_img()
		Utils.log("INFO", "验证码为 %s" % self.pdata['ValidCode'])

		Utils.log("INFO", "登录中 ...")
		self.operate = self._get_response(iconfig.LOGINURL, self.pdata)
		curl_url = self.operate.geturl()
		web_content = self.operate.read()
		Utils.log("INFO", "curl_url: %s" % curl_url)
		Utils.log("INFO", "web_content: %s" % web_content)

		return

	# 获取验证码图片
	def _get_icode_img(self):
		icode_img = self._get_response(iconfig.ICODEURL)
		self._write_file('../resources/EasternPioneer-icode.png', icode_img)

	# 识别验证码图片
	def _identify_icode_img(self):
		if iconfig.AUTO_IDENTIFY_ICODE:
			icode_image = Image.open('../resources/EasternPioneer-icode.png')
			self.pdata['ValidCode'] = pytesseract.image_to_string(icode_image)
		else:
			self.pdata['ValidCode'] = raw_input("请输入验证码: ")


	def _get_response(self, url, data = None):
		if data is not None:
			req = urllib2.Request(url, urllib.urlencode(data))
		else:
			req = urllib2.Request(url)

		response = self.opener.open(req)
		return response

	# 写文件
	def _write_file(self, filename, data):
		try:
			output_file = open(filename, 'wb')
			output_file.writelines(data)
			output_file.close()
			Utils.log("INFO", '文件 %s 写入完成' % filename)
		except IOError:
			Utils.log("ERROR", "写文件失败")