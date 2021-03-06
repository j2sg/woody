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
from model.user import User
from model.note import Note

class PumpController(object):
    def __init__(self, account, callback = None):
        client = pypump.Client(webfinger = account.name, name = 'Woody4Pump', type = 'native')

        self._api = pypump.PyPump(client = client, verifier_callback = callback)

    def me(self):
        if not self._api:
            return None

        return self.user(self._api.me.webfinger)


    def user(self, id):
        if not self._api or not id:
            return None

        res = self._api.Person(id)

        return User(res.webfinger,
                    res.display_name.encode('utf-8'),
                    res.summary.encode('utf-8'),
                    res.location.display_name.encode('utf-8')) if res is not None else None


    def timeline(self, limit = 0):
        if not self._api:
            return None

        notes = []

        for activity in self._api.me.inbox.major[:limit]:
            author = User(activity.actor.webfinger,
                          activity.actor.display_name.encode('utf-8'),
                          activity.actor.summary.encode('utf-8'),
                          activity.actor.location.display_name.encode('utf-8'))

            note = Note(activity.obj.url, author, activity.published, activity.obj.content.encode('utf-8') if activity.obj.content is not None else '')
            note.source = str(activity.generator)

            notes.append(note)

        return notes


    def userTimeline(self, id, limit = 0):
        if not self._api or not id:
            return None

        notes = []

        for activity in self._api.Person(id).outbox.major[:limit]:
            author = User(activity.actor.webfinger,
                          activity.actor.display_name.encode('utf-8'),
                          activity.actor.summary.encode('utf-8'),
                          activity.actor.location.display_name.encode('utf-8'))

            note = Note(activity.obj.url, author, activity.published, activity.obj.content.encode('utf-8') if activity.obj.content is not None else '')
            note.source = str(activity.generator)

            notes.append(note)

        return notes


    def receivedMessages(self):
        pass


    def sentMessages(self):
        pass


    def sendMessage(self, message):
        pass


    def following(self):
        if not self._api:
            return None

        users = []

        for friend in self._api.me.following:
            user = User(friend.webfinger,
                        friend.display_name.encode('utf-8'),
                        friend.summary.encode('utf-8'),
                        friend.location.display_name.encode('utf-8'))
            users.append(user)

        return users


    def followers(self):
        if not self._api:
            return None

        users = []

        for friend in self._api.me.followers:
            user = User(friend.webfinger,
                        friend.display_name.encode('utf-8'),
                        friend.summary.encode('utf-8'),
                        friend.location.display_name.encode('utf-8'))
            users.append(user)

        return users


    def follow(self, user):
        if not self._api or not user:
            return False

        self._api.Person(user.id).follow()

        return True


    def unfollow(self, user):
        if not self._api or not user:
            return False

        self._api.Person(user.id).unfollow()

        return True


    def block(self, user):
        return None


    def unblock(self, user):
        return None


    def post(self, note):
        if not self._api or not note:
            return False

        res = self._api.Note(note.content)
        res.to = self._api.Public
        res.cc = (self._api.me.followers)

        res.send()

        note.id = res.url
        note.author = User(res.author.webfinger,
                           res.author.display_name.encode('utf-8'),
                           res.author.summary.encode('utf-8'),
                           res.author.location.display_name.encode('utf-8'))
        note.date = res.published

        return True


    def share(self, note):
        pass


    def like(self, note):
        pass


    def unlike(self, note):
        pass
