#!/usr/bin/env python
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

"Usage: %s <command> [param ...]"

import sys

from persistence.persistencemanager import PersistenceManager
from model.account import OAuthAccount
from net.twittercontroller import TwitterController


def main():
	command, params = processArgs()

	if not command:
		print __doc__ % sys.argv[0]
		sys.exit(1)

	initApp()
	execCommand(command, params)
	

def initApp():
	pm = PersistenceManager()
	if not pm.existsConfig():
		pm.createConfig()


def processArgs():
	commands = {'CREATE_ACCOUNT' : 2,
                    'REGISTER_ACCOUNT' : 1,
                    'DELETE_ACCOUNT' : 1,
                    'LIST_ACCOUNTS' : 0}
	command = None
	params = []

	if len(sys.argv) < 2:
		return (None, None)

	for arg in sys.argv[1:]:
		if arg[0] == '-':
			if command:
				return (None, None)
			if arg == '-c' or arg == '--create-account':
				command = 'CREATE_ACCOUNT'
			elif arg == '-r' or arg == '--register-account':
				command = 'REGISTER_ACCOUNT'
			elif arg == '-d' or arg == '--del-account':
				command = 'DELETE_ACCOUNT'
			elif arg == '-l' or arg == '--list-accounts':
				command = 'LIST_ACCOUNTS'
			else:
				return (None, None)
		elif command:
			params.append(arg)
		else:
			return (None, None)

	if len(params) != commands[command]:
		return (None, None)
			
	return (command, params)


def execCommand(cmd, args):
	pass


def listAccounts():
	pm = PersistenceManager()
	accounts = pm.readConfig()['accounts']
	print accounts


def register(url = None):
	if url:
		print(url)
	return raw_input('Verifier:')
	
	
if __name__ == '__main__':
	main()
