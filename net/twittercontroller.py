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

from tweepy import OAuthHandler
from tweepy import API

class TwitterControllerAuthException(Exception):
	def __init__(self, msg):
		self.msg = msg

class TwitterController(object):
	consumerToken = 'jEvfZyViQyTIgnUyYfrCIgLkE'
	consumerSecret = 'bauGmd2ecotJzWjYHMML4X5HUHaNS6z4FtWZ68e6JikOQ1PkSO'

	def __init__(self, account = None):
		self.account = account
		self._authHandler = OAuthHandler(TwitterController.consumerToken, TwitterController.consumerSecret)
		self._api = None

	def verify(self):
		return self._authHandler.get_authorization_url()

	def register(self, verifier):
		self._authHandler.get_access_token(verifier)

	def auth(self):
		if self.account is None:
			raise TwitterControllerAuthException('TwitterController :: Auth :: Account is not set yet')
		
		if not self.account.key or not self.account.secret:
			raise TwitterControllerAuthException('TwitterController :: Auth :: Tokens are not set yet')

		self._authHandler.set_access_token(self.account.key, self.account.secret)
		self._api = API(self._authHandler)
			

	def getTimeline(self, length = 10):
		return []

	def getFollowers(self):
		return []

	def getFollowing(self):
		return []

	def post(self, message):
		if self._api:
			self._api.update_status(message)


