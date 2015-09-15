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
from model.user import User
from model.note import Note

# Twitter Controller for API 1.1 https://dev.twitter.com/overview/api

class TwitterController(object):
    consumerToken = 'jEvfZyViQyTIgnUyYfrCIgLkE'
    consumerSecret = 'bauGmd2ecotJzWjYHMML4X5HUHaNS6z4FtWZ68e6JikOQ1PkSO'


    def __init__(self, account, callback = None):
        authHandler = tweepy.OAuthHandler(TwitterController.consumerToken, TwitterController.consumerSecret)

        if not account.isRegistered():
            verifier = callback(authHandler.get_authorization_url())
            authHandler.get_access_token(verifier)
            if tweepy.__version__ < '3.2.0':
                account.key, account.secret = authHandler.access_token.key, authHandler.access_token.secret
            else:
                account.key, account.secret = authHandler.access_token, authHandler.access_token_secret
        else:
            authHandler.set_access_token(account.key, account.secret)

        self._api = tweepy.API(authHandler)


    def me(self):
        if not self._api:
            return None

        res = self._api.me()

        return self.user(res.screen_name)


    def user(self, id):
        if not self._api or not id:
            return None

        res = self._api.get_user(screen_name = id)

        return User(res.screen_name,
                    res.name.encode('utf-8'),
                    res.description.encode('utf-8'),
                    res.location.encode('utf-8'),
                    res.friends_count,
                    res.followers_count,
                    res.statuses_count,
                    res.favourites_count) if res is not None else None


    def timeline(self, limit = 0):
        if not self._api:
            return None

        notes = []

        for tweet in tweepy.Cursor(self._api.home_timeline).items(limit):
            author = User(tweet.user.screen_name,
                          tweet.user.name.encode('utf-8'),
                          tweet.user.description.encode('utf-8'),
                          tweet.user.location.encode('utf-8'),
                          tweet.user.friends_count,
                          tweet.user.followers_count,
                          tweet.user.statuses_count,
                          tweet.user.favourites_count)

            note = Note(tweet.id_str, author, tweet.created_at, tweet.text.encode('utf-8'))

            note.replyto = self.user(tweet.in_reply_to_screen_name)
            note.source = tweet.source.encode('utf-8')
            note.shares = tweet.retweet_count
            note.likes = tweet.favorite_count

            notes.append(note)

        return notes


    def userTimeline(self, id, limit = 0):
        if not self._api or not id:
            return None

        res = self._api.user_timeline(screen_name = id, count = limit)

        if not res:
            return None

        notes = []

        for tweet in res:
            author = User(tweet.user.screen_name,
                          tweet.user.name.encode('utf-8'),
                          tweet.user.description.encode('utf-8'),
                          tweet.user.location.encode('utf-8'),
                          tweet.user.friends_count,
                          tweet.user.followers_count,
                          tweet.user.statuses_count,
                          tweet.user.favourites_count)

            note = Note(tweet.id_str, author, tweet.created_at, tweet.text.encode('utf-8'))

            note.replyto = self.user(tweet.in_reply_to_screen_name)
            note.source = tweet.source.encode('utf-8')
            note.shares = tweet.retweet_count
            note.likes = tweet.favorite_count

            notes.append(note)

        return notes


    def receivedMessages(self):
        if not self._api:
            return None

        messages = []

        for msg in tweepy.Cursor(self._api.direct_messages).items():
            author = User(msg.sender.screen_name,
                          msg.sender.name.encode('utf-8'),
                          msg.sender.description.encode('utf-8'),
                          msg.sender.location.encode('utf-8'),
                          msg.sender.friends_count,
                          msg.sender.followers_count,
                          msg.sender.statuses_count,
                          msg.sender.favourites_count)

            message = Note(msg.id_str, author, msg.created_at, msg.text.encode('utf-8'))

            messages.append(message)

        return messages


    def sentMessages(self):
        if not self._api:
            return None

        messages = []

        for msg in tweepy.Cursor(self._api.sent_direct_messages).items():
            receiver = User(msg.recipient.screen_name,
                            msg.recipient.name.encode('utf-8'),
                            msg.recipient.description.encode('utf-8'),
                            msg.recipient.location.encode('utf-8'),
                            msg.recipient.friends_count,
                            msg.recipient.followers_count,
                            msg.recipient.statuses_count,
                            msg.recipient.favourites_count)

            message = Note(msg.id_str, receiver, msg.created_at, msg.text.encode('utf-8'))

            messages.append(message)

        return messages


    def sendMessage(self, message):
        if not self._api or not message:
            return False

        res = self._api.send_direct_message(screen_name = message.author.id, text = message.content)

        if not res:
            return False

        message.id = res.id_str
        message.date = res.created_at

        return True


    def following(self):
        if not self._api:
            return None

        users = []

        for friend in tweepy.Cursor(self._api.friends).items():
            user = User(friend.screen_name,
                        friend.name.encode('utf-8'),
                        friend.description.encode('utf-8'),
                        friend.location.encode('utf-8'),
                        friend.friends_count,
                        friend.followers_count,
                        friend.statuses_count,
                        friend.favourites_count)

            users.append(user)

        return users

    def followers(self):
        if not self._api:
            return None

        users = []

        for follower in tweepy.Cursor(self._api.followers).items():
            user = User(follower.screen_name,
                        follower.name.encode('utf-8'),
                        follower.description.encode('utf-8'),
                        follower.location.encode('utf-8'),
                        follower.followers_count,
                        follower.followers_count,
                        follower.statuses_count,
                        follower.favourites_count)

            users.append(user)

        return users


    def follow(self, user):
        if not self._api or not user:
            return False

        res = self._api.create_friendship(screen_name = user.id)

        if not res:
            return False

        user.following = res.friends_count

        return True


    def unfollow(self, user):
        if not self._api or not user:
            return False

        res = self._api.destroy_friendship(screen_name = user.id)

        if not res:
            return False

        user.following = res.friends_count

        return True


    def block(self, user):
        if not self._api or not user:
            return False

        return self._api.create_block(screen_name = user.id) is not None


    def unblock(self, user):
        if not self._api or not user:
            return False

        return self._api.destroy_block(screen_name = user.id) is not None


    def post(self, note):
        if not self._api or not note:
            return False

        res = self._api.update_status(status = note.content)

        if not res:
            return False

        note.id = res.id_str
        note.author = User(res.user.screen_name,
                           res.user.name.encode('utf-8'),
                           res.user.description.encode('utf-8'),
                           res.user.location.encode('utf-8'),
                           res.user.friends_count,
                           res.user.followers_count,
                           res.user.statuses_count,
                           res.user.favourites_count)
        note.date = res.created_at

        return True


    def share(self, note):
        if not self._api or not note:
            return False

        res = self._api.retweet(note.id)

        if not res:
            return False

        note.shares = res.retweet_count

        return True


    def like(self, note):
        if not self._api or not note:
            return False

        res = self._api.create_favorite(note.id)

        if not res:
            return False

        note.likes += 1

        return True


    def unlike(self, note):
        if not self._api or not note:
            return False

        return self._api.destroy_favorite(note.id) is not None

        if not res:
            return False

        note.likes -= 1

        return True
