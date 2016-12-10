# -*- coding: utf-8 -*-

from websites import EasternPioneer

if __name__ == "__main__":
	ep = EasternPioneer()

	ep.login("11105291", "10090")

	ep.book()
