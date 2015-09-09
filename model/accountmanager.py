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

from account import Account
from account import OAuthAccount
from account import UserPassAccount
from persistence.persistencemanager import PersistenceManager
from net.twittercontroller import TwitterController
from net.pumpcontroller import PumpController

class AccountManager(object):
    def create(self, account):
        if not Account.hasSupport(account.network):
            return False

        if self.exists(account):
            return False

        pm = PersistenceManager()

        if not pm.existsConfig():
            return False

        config = pm.readConfig()

        accountType = Account.networkToAccount(account.network)

        if accountType == 'OAuth':
            config['accounts'][account.network].append(dict(name = account.name,key = account.key, secret = account.secret))
        elif accountType == 'UserPass':
            config['accounts'][account.network].append(dict(name = account.name,user = account.user, password = account.password))

        pm.writeConfig(config)

        return True


    def register(self, account, callback):
        if not Account.hasSupport(account.network):
            return False

        if not self.exists(account):
            return False

        pm = PersistenceManager()

        if not pm.existsConfig():
            return False

        config = pm.readConfig()

        controller = None

        if account.network == 'twitter':
            controller = TwitterController(account, callback)
        elif account.network == 'pump.io':
            controller = PumpController(account, callback)

        if not controller:
            return False

        return self.modify(account)


    def modify(self, account, newname = None):
        if not Account.hasSupport(account.network):
            return False

        if not self.exists(account):
            return False

        pm = PersistenceManager()

        if not pm.existsConfig():
            return False

        config = pm.readConfig()

        accountType = Account.networkToAccount(account.network)

        for entry in config['accounts'][account.network]:
            if entry['name'] == account.name:
                if newname:
                    entry['name'] = newname
                if accountType == 'OAuth':
                    entry['key'], entry['secret'] = account.credentials()
                elif accountType == 'UserPass':
                    entry['user'], entry['password'] = account.credentials()

                break

        pm.writeConfig(config)

        return True

    def remove(self, account):
        if not Account.hasSupport(account.network):
            return False

        if not self.exists(account):
            return False

        pm = PersistenceManager()

        if not pm.existsConfig():
            return False

        config = pm.readConfig()

        entry = None

        for k in range(len(config['accounts'][account.network])):
            entry = config['accounts'][account.network][k]

            if entry['name'] == account.name:
                break

        config['accounts'][account.network].remove(entry)

        pm.writeConfig(config)

        return True

    def get(self, network, name):
        for account in self.getAllByNetwork(network):
            if account.name == name:
                return account

        return None


    def getAllByNetwork(self, network):
        if not Account.hasSupport(network):
            return None

        pm = PersistenceManager()

        if not pm.existsConfig():
            return None

        config = pm.readConfig()

        accounts = []
        accountType = Account.networkToAccount(network)

        for entry in config['accounts'][network]:
            account = Account.getAccount(network, entry['name'])

            if accountType == 'OAuth':
                account.setCredentials((entry['key'], entry['secret']))
            elif accountType == 'UserPass':
                account.setCredentials((entry['user'], entry['password']))

            accounts.append(account)

        return accounts


    def getAll(self):
        accounts = []

        for network in Account.supportedNetworks():
            accounts.extend(self.getAllByNetwork(network))

        return accounts


    def exists(self, account):
        return not self.get(account.network, account.name) is None
