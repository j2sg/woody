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

class ControllerException(Exception):
        def __init__(self, msg):
                self.msg = msg

class NoAccessTokenException(ControllerException):
	def __init__(self, msg, account, url):
		super(TwitterControllerException, self).__init__(msg)
		self.account = account
		self.url = url

