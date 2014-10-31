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

from net.controller import Controller

class Account(object):
	def __init__(self, network, name):
		if not network in Controller.supported:
			raise Exception('Protocol {} not supported'.format(network))

		self.network = network
		self.name = name

class OAuthAccount(Account):
	def __init__(self, network, name, key, secret):
		super(OAuthAccount, self).__init__(network, name)
		self.key = key
		self.secret = secret

class UserPassAccount(Account):
	def __init__(self, network, name, user, password):
		super(UserPassAccount, self).__init__(network, name)
		self.user = user
		self.password = password
