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

import atributes
from PyQt4.QtCore import QSettings

class PersistenceManager:
	def __init__(self):
		self.settings = QSettings(atributes.ORGANIZATION_NAME, atributes.APPLICATION_NAME)

	def existsConfig(self):
		return self.settings.value('Executed', False).toBool()

	def createConfig(self, overwrite = False):
		if self.existsConfig() and not overwrite:
			return False

		self.settings.setValue('Executed', True)

		return True

	def deleteConfig(self):
		if not self.existsConfig():
			return False

		self.settings.clear()

		return True

	def readConfig(self, key, group = None):
		if not self.existsConfig():
			return None

		if not group is None:
			self.settings.beginGroup(group)
		value = self.settings.value(key)
		if not group is None:
			self.settings.endGroup()
		
		return value
		

	def writeConfig(self, value, key, group = None):
		if not self.existsConfig():
			return False

		if not group is None:
			self.settings.beginGroup(group)
		if not self.settings.contains(key):
			return False
		self.settings.setValue(key, value)
		if not group is None:
			self.settings.endGroup()

		return True

