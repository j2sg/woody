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

class Account(object):
    supported = {'OAuth'    : ['twitter'],
                 'UserPass' : []}


    def __init__(self, network, name):
        self.network = network
        self.name = name


    @classmethod
    def getAccount(cls, network, name):
        account = cls.networkToAccount(network)

        if account == 'OAuth':
            return OAuthAccount(network, name)
        elif account == 'UserPass':
            return UserPassAccount(network, name)

        return None


    @classmethod
    def supportedNetworks(cls):
        networks = []

        for account in cls.supported:
            networks.extend(cls.supported[account])

        return networks


    @classmethod
    def hasSupport(cls, network):
        for account in cls.supported:
            if network in cls.supported[account]:
                return True

        return False


    @classmethod
    def networkToAccount(cls, network):
        for account in cls.supported:
            if network in cls.supported[account]:
                return account

        return None


    @classmethod
    def accountToNetworks(cls, account):
        if account in cls.supported.keys():
            return cls.supported[account]

        return None


class OAuthAccount(Account):
    def __init__(self, network, name, key = None, secret = None):
        super(OAuthAccount, self).__init__(network, name)
        self.key = key
        self.secret = secret


class UserPassAccount(Account):
    def __init__(self, network, name, user = None, password = None):
        super(UserPassAccount, self).__init__(network, name)
        self.user = user
        self.password = password
