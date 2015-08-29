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

import tweepy

class TwitterController(object):
    consumerToken = 'jEvfZyViQyTIgnUyYfrCIgLkE'
    consumerSecret = 'bauGmd2ecotJzWjYHMML4X5HUHaNS6z4FtWZ68e6JikOQ1PkSO'


    def __init__(self, account, callback = None):
        authHandler = tweepy.OAuthHandler(TwitterController.consumerToken, TwitterController.consumerSecret)

        if not account.isRegistered():
            verifier = callback(authHandler.get_authorization_url())
            authHandler.get_access_token(verifier)
            account.key, account.secret = authHandler.access_token.key, authHandler.access_token.secret
        else:
            authHandler.set_access_token(account.key, account.secret)

        self._api = tweepy.API(authHandler)


    def me(self):
        if not self._api:
            return None

        return self._api.me()


    def user(self, id):
        if not self._api:
            return None

        return self._api.get_user(screen_name = id)


    def timeline(self, limit = 0):
        if not self._api:
            return None

        return tweepy.Cursor(self._api.home_timeline).items(limit)


    def userTimeline(self, id, limit = 0):
        if not self._api:
            return None

        return self._api.user_timeline(screen_name = id, count = limit)


    def receivedMessages(self):
        if not self._api:
            return None

        return tweepy.Cursor(self._api.direct_messages).items()


    def sentMessages(self):
        if not self._api:
            return None

        return tweepy.Cursor(self._api.sent_direct_messages).items()


    def sendMessage(self, id, message):
        if not self._api:
            return None

        return self._api.send_direct_message(screen_name = id, text = message)


    def followers(self):
        if not self._api:
            return None

        return tweepy.Cursor(self._api.followers).items()


    def following(self):
        if not self._api:
            return None

        return tweepy.Cursor(self._api.friends).items()


    def post(self, message):
        if not self._api:
            return None

        return self._api.update_status(message)


    def share(self, id):
        if not self._api:
            return None

        return self._api.retweet(id)


    def like(self, id):
        if not self._api:
            return None

        return self._api.create_favorite(id)
