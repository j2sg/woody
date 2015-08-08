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

import sys
import atributes

from model.account import Account
from model.accountmanager import AccountManager

class CommandLine(object):
    def execute(self):
        command, params = self.processArgs()

        if not command:
            print __doc__ % sys.argv[0]
            print 'Use -h --help option to get more details'
            sys.exit(1)


        self.execCommand(command, params)


    def processArgs(self):
        commands = {'CREATE_ACCOUNT' : 2,
                    'REGISTER_ACCOUNT' : 2,
                    'DELETE_ACCOUNT' : 2,
                    'LIST_ACCOUNTS' : 0,
                    'HELP' : 0}
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
                elif arg == '-d' or arg == '--delete-account':
                    command = 'DELETE_ACCOUNT'
                elif arg == '-l' or arg == '--list-accounts':
                    command = 'LIST_ACCOUNTS'
                elif arg == '-h' or arg == '--help':
                    command = 'HELP'
                else:
                    return (None, None)
            elif command:
                params.append(arg)
            else:
                return (None, None)

        if len(params) != commands[command]:
            return (None, None)

        return (command, params)


    def execCommand(self, cmd, args):
        am = AccountManager()

        if cmd == 'CREATE_ACCOUNT':
            account = Account.getAccount(args[0], args[1])
            if account and am.create(account):
                print 'Created {0} account {1}'.format(account.network, account.name)
            else:
                print 'There was an error during creation'
        elif cmd == 'DELETE_ACCOUNT':
            account = Account.getAccount(args[0], args[1])
            if account and am.remove(account):
                print 'Removed {0} account {1}'.format(account.network, account.name)
            else:
                print 'There was an error during elimination'
        elif cmd == 'LIST_ACCOUNTS':
            for account in am.getAll():
                print '{0} account {1}'.format(account.network, account.name)
        elif cmd == 'HELP':
            self.help()


    def register(self, url = None):
        if url:
            print(url)

        return raw_input('Verifier:')


    def help(self):
        print '{0} {1} - {2}'.format(atributes.APPLICATION_NAME, atributes.APPLICATION_VERSION, atributes.APPLICATION_DESC)
        print '\n\tUsage: {0} <command> [param ...]'.format(sys.argv[0])
        print '\nCOMMANDS'
        print '\n\t -c --create-account <network> <name>\tCreate a new social network account'
        print '\n\t -r --register-account <network> <name>\t\tRegister an existing account'
        print '\n\t -d --delete-account <network> <name>\t\tDelete an existing account'
        print '\n\t -l --list-accounts\t\t\tList all accounts'
        print '\n\t -h --help\t\t\t\tShow this help message\n'
