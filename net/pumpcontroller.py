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

        res = self._api.me

        return self.user(res.webfinger)


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
        pass


    def receivedMessages(self):
        pass


    def sentMessages(self):
        pass


    def sendMessage(self, message):
        pass


    def following(self):
        pass


    def followers(self):
        pass


    def follow(self, user):
        pass


    def unfollow(self, user):
        pass


    def block(self, user):
        pass


    def unblock(self, user):
        pass


    def post(self, note):
        pass


    def share(self, note):
        pass


    def like(self, note):
        pass


    def unlike(self, note):
        pass
