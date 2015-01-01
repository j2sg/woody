#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  This file is part of Woody.
#
#  Copyright (c) 2014 Juan Jose Salazar Garcia jjslzgc@gmail.com
#
#  Woody is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Woody is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Woody.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import atributes
from PyQt4.QtGui import QApplication
from view.mainwindow import MainWindow
from persistence.persistencemanager import PersistenceManager
from model.account import OAuthAccount
from net.twittercontroller import TwitterController

def main():
	app = QApplication(sys.argv)
	
	initApplication(app)
	
	if not verifyConfig():
		print 'It has been occurred errors during config verification. Exit NOW!!!'
		exit()

	window = MainWindow()
	window.show()
	
	app.exec_()

def initApplication(app):
	app.setOrganizationName(atributes.ORGANIZATION_NAME)
	app.setOrganizationDomain(atributes.ORGANIZATION_DOMAIN)
	app.setApplicationName(atributes.APPLICATION_NAME)
	app.setApplicationVersion(atributes.APPLICATION_VERSION)

def verifyConfig():
        pm = PersistenceManager()
	
	if not pm.existsConfig() and not pm.createConfig():
		return False

	return True

if __name__ == '__main__':
	main()
