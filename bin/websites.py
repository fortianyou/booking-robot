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
		self.login_pdata = {
			'AjaxMethod' : 'LOGIN',
			'Account' : '',
			'Pwd' : '',
			'ValidCode' : ''
		}

		self.query_pdata = {
			'loginType':'2',
			'method':'stu',
			'stuid':'',
			'sfznum':'',
			'carid':'',
			'ValidCode':''
		}

		self.book_pdata = {
			'loginType' : '2',
			'method' : 'yueche',
			'stuid' : '',
			'bmnum' : 'BD15111000359',
			'start' : 7,
			'end' : 9,
			'lessionid' : '001',
			'trainpriceid' : 'BD13062500001',
			'lesstypeid' : '02',
			'date' : '2016-12-10',
			'id' : '1',
			'carid' : '',
			'ycmethod' : '03',
			'cartypeid' : '02',
			'trainsessionid' : '01',
			'ReleaseCarID' : '',
			'ValidCode' : ''
		}

		self.is_booking = True # 是否继续预订
		self.is_login = False # 是否已登录

		self.operate = '' # response对象(不含read)
		self.cj = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		urllib2.install_opener(self.opener)
		
		return

	# 登录
	def login(self, account='', password=''):
		self.login_pdata['Account'] = account
		self.login_pdata['Pwd'] = password

		while not self.is_login:
			Utils.log("INFO", "登录中 ...")

			Utils.log("INFO", "获取登录验证码中 ...")
			self._get_icode_img(iconfig.LOGIN_ICON_URL, "EasternPioneer-login-icon.png")

			Utils.log("INFO", "识别登录验证码中 ...")
			self.login_pdata['ValidCode'] = self._identify_icode_img("EasternPioneer-login-icon.png")
			Utils.log("INFO", "登录验证码为 %s" % self.login_pdata['ValidCode'])

			Utils.log("INFO", "登录中 ...")
			self.operate = self._get_response(iconfig.LOGIN_URL, self.login_pdata)
			web_content = self.operate.read()
			if web_content == iconfig.LOGIN_RESPONSE['success']:
				Utils.log("INFO", "登录成功(%s)" % web_content)
				self.is_login = True
			else:
				Utils.log("ERROR", "登录失败，重新登录(%s)" % web_content)

		return

	# 约车
	def book(self):
		Utils.log("INFO", "获取约车验证码中 ...")
		self._get_icode_img(iconfig.BOOK_ICON_URL, "EasternPioneer-book-icon.png")

		Utils.log("INFO", "识别约车验证码中 ...")
		self.query_pdata['ValidCode'] = self._identify_icode_img("EasternPioneer-book-icon.png")
		self.book_pdata['ValidCode'] = self.query_pdata['ValidCode']
		Utils.log("INFO", "约车验证码为 %s" % self.book_pdata['ValidCode'])

		self.query_pdata['stuid'] = self.login_pdata['Account']
		self.book_pdata['stuid'] = self.login_pdata['Account']

		Utils.log("INFO", "查询中 ...")
		self.operate = self._get_response(iconfig.BOOK_URL + Utils.dict2str(self.query_pdata), self.query_pdata)
		web_content = self.operate.read()
		Utils.log("INFO", "查询结束(%s)" % web_content)

		for date in iconfig.BOOK_DATE:
			for period in iconfig.BOOK_PERIOD:
			
				self.book_pdata['start'] = iconfig.BOOK_START_HOUR[period]
				self.book_pdata['end'] = iconfig.BOOK_END_HOUR[period]
				self.book_pdata['date'] = date
				self.book_pdata['trainsessionid'] = period

				Utils.log("INFO", "即将预订：日期(%s), 时间段(%s), POST(%s)" % (date, period, Utils.dict2str(self.book_pdata)))

				self.operate = self._get_response(iconfig.BOOK_URL + Utils.dict2str(self.book_pdata), self.book_pdata)
				web_content = self.operate.read()
				Utils.log("INFO", "预订结束(%s)" % web_content)

	# 获取验证码图片
	def _get_icode_img(self, url, fname):
		icode_img = self._get_response(url)
		self._write_file("../resources/%s" % fname, icode_img)

	# 识别验证码图片
	def _identify_icode_img(self, fname):
		if iconfig.AUTO_IDENTIFY_ICODE:
			icode_image = Image.open("../resources/%s" % fname)
			return pytesseract.image_to_string(icode_image)
		else:
			return raw_input("请输入验证码: ")

	# 获取响应
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