# -*- coding: utf-8 -*-

LOGIN_URL = r'http://wsyc.dfss.com.cn/DfssAjax.aspx'
LOGIN_ICON_URL = r'http://wsyc.dfss.com.cn/validpng.aspx?aa=3&page=lg'
BOOK_URL = r'http://wsyc.dfss.com.cn/Ajax/StuHdl.ashx?'
BOOK_ICON_URL = r'http://wsyc.dfss.com.cn/validpng.aspx'

AUTO_IDENTIFY_ICODE = False

LOGIN_RESPONSE = {
	'success' : 'true'
}

BOOK_DATE = ['2016-12-18']

BOOK_PERIOD = ['03','04','02']

BOOK_START_HOUR = {
	'01' : 7,
	'02' : 9,
	'03' : 13,
	'04' : 17,
	'05' : 19
}

BOOK_END_HOUR = {
	'01' : 9,
	'02' : 13,
	'03' : 17,
	'04' : 19,
	'05' : 21
}
