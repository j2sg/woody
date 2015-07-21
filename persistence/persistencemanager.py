# -*- coding: utf-8 -*-

#
#  This file is part of Woody.
#
#  Copyright (c) 2014-2015 Juan Jose Salazar Garcia jjslzgc@gmail.com
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

import os
import json

class PersistenceManager(object):
	configFileName = 'config.json'
	def existsConfig(self):
        	return os.path.isfile(PersistenceManager.configFileName)

	
	def createConfig(self, overwrite = False):
		if self.existsConfig() and not overwrite:
			return False
		
		config = {
                          'app' : {}, 
                          'accounts' : []
                         }
		
		with open(PersistenceManager.configFileName, 'w') as configFile:
			json.dump(config, configFile, indent = 3)

		return True

	
	def deleteConfig(self):
		if not self.existsConfig():
			return False

		os.remove(PersistenceManager.configFileName)

		return True

	def readConfig(self):
		config = None
		
		if self.existsConfig():
			with open(PersistenceManager.configFileName) as configFile:
				config = json.load(configFile)

		return config


	def writeConfig(self, config):
		with open(PersistenceManager.configFileName, 'w') as configFile:
			json.dump(config, configFile, indent = 3)



