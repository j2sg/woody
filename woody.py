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

from persistence.persistencemanager import PersistenceManager
from model.account import OAuthAccount
from net.twittercontroller import TwitterController


def main():
	persistenceManager = PersistenceManager()


def register(url = None):
	if url:
		print(url)
	return raw_input('Verifier:')
	
	
if __name__ == '__main__':
	main()
