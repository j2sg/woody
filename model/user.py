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

class User(object):
    def __init__(self, id, name = '', bio = None, location = None, following = 0, followers = 0, notes = 0, likes = 0):
        self.id = id
        self.name = name
        self.bio = bio
        self.location = location
        self.following = following
        self.followers = followers
        self.notes = notes
        self.likes = likes

    def __str__(self):
        return '\n\t{0} (@{1}) {2}\n\tLocation: {3}\n\tFollowing: {4} Followers: {5} Notes: {6} Likes: {7}'.format(self.name,
                                                                                                                   self.id,
                                                                                                                   '' if self.bio is None else '\n\t' + self.bio,
                                                                                                                   self.location,
                                                                                                                   self.following,
                                                                                                                   self.followers,
                                                                                                                   self.notes,
                                                                                                                   self.likes)
