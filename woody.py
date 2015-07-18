#!/usr/bin/env python3
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

from model.account import OAuthAccount
#from net.twittercontroller import TwitterController
from net.pumpcontroller import PumpController

def register(url = None):
	if url:
		print(url)
	return raw_input('Verifier:')

def main():
	#twitterAccount = OAuthAccount('Twitter', 'Test account')
	#twitterController = TwitterController(twitterAccount, register)
	#
	#print 'Access Token: ', twitterAccount.key
	#print 'Access Token Secret: ', twitterAccount.secret
	#
	#print '### Timeline (10 last tweets) ###'
	#for tweet in twitterController.timeline(10):
	#	print tweet.text
	#
	#print '### Followers ###'
	#for follower in twitterController.followers():
	#	print follower.screen_name
	#
	#print '### Following ###'
	#for following in twitterController.following():
	#	print following.screen_name
	pumpAccount = OAuthAccount('Pump.io', 'woodytester@microca.st')
	pumpController = PumpController(pumpAccount, register)
	print(pumpController.timeline(10))


if __name__ == '__main__':
	main()
