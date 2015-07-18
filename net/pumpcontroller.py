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

import pypump

class PumpController(object):
	def __init__(self, account, callback = None):
		client = pypump.Client(webfinger=account.name, name='Woody4Pump', type='native')
		self._api = pypump.PyPump(client=client, verifier_callback=callback)

			
	def timeline(self, limit = 0):
		return self._api.me.outbox[:limit]


	def followers(self):
		return self._api.me.followers


	def following(self):
		return self._api.me.following


	def post(self, message):
		pass

