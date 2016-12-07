# -*- coding: utf-8 -*-

from websites import EasternPioneer

if __name__ == "__main__":
	ep = EasternPioneer()

	ep.login("1110000", "00000")

	ep.book()