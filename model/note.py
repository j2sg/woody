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

from model.user import User

class Note(object):
    def __init__(self, id, author, date, content):
        self.id = id
        self.author = author
        self.date = date
        self.content = content
        self.to = None
        self.cc = None
        self.replyto = None
        self.source = None
        self.shares = None
        self.likes = None


    def __str__(self):
        return '\n\t{0} (@{1}) {2}{3} via {4}\n\t\t{5}\n\tID: {6} Shares: {7} Likes: {8}'.format(self.author.name,
                                                                                                 self.author.id,
                                                                                                 self.date,
                                                                                                 ' in reply to ' + self.replyto.id if self.replyto is not None else '',
                                                                                                 self.source,
                                                                                                 self.content,
                                                                                                 self.id,
                                                                                                 self.shares,
                                                                                                 self.likes)
