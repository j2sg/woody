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

"Usage: %s <command> [param ...]"

import sys
import atributes

from model.account import Account
from model.accountmanager import AccountManager

class CommandLine(object):
    def execute(self):
        command, params = self.processArgs()

        if not command:
            print __doc__ % sys.argv[0]
            print 'Use -h --help option to get more details'
            sys.exit(1)


        self.execCommand(command, params)


    def processArgs(self):
        commands = {'NETWORKS' : [0,0],
                    'CREATE_ACCOUNT' : [2,2],
                    'REGISTER_ACCOUNT' : [2,2],
                    'DELETE_ACCOUNT' : [2,2],
                    'LIST_ACCOUNTS' : [0,1],
                    'ME' : [2,2],
                    'TIMELINE' : [2,3],
                    'RECEIVED_MESSAGES' : [2,2],
                    'SENT_MESSAGES' : [2,2],
                    'SEND_MESSAGE' : [4,4],
                    'FOLLOWING' : [2,2],
                    'FOLLOWERS' : [2,2],
                    'FOLLOW' : [3,3],
                    'UNFOLLOW' : [3,3],
                    'BLOCK' : [3,3],
                    'UNBLOCK' : [3,3],
                    'POST' : [3,3],
                    'SHARE' : [3,3],
                    'LIKE' : [3,3],
                    'UNLIKE' : [3,3],
                    'USER' : [3,3],
                    'USER_TIMELINE' : [3,4],
                    'HELP' : [0,0]}
        command = None
        params = []

        if len(sys.argv) < 2:
            return (None, None)

        for arg in sys.argv[1:]:
            if arg[0] == '-':
                if command:
                    return (None, None)
                if arg == '-n' or arg == '--networks':
                    command = 'NETWORKS'
                elif arg == '-c' or arg == '--create-account':
                    command = 'CREATE_ACCOUNT'
                elif arg == '-r' or arg == '--register-account':
                    command = 'REGISTER_ACCOUNT'
                elif arg == '-d' or arg == '--delete-account':
                    command = 'DELETE_ACCOUNT'
                elif arg == '-l' or arg == '--list-accounts':
                    command = 'LIST_ACCOUNTS'
                elif arg == '-m' or arg == '--me':
                    command = 'ME'
                elif arg == '-t' or arg == '--timeline':
                    command = 'TIMELINE'
                elif arg == '-R' or arg == '--received-messages':
                    command = 'RECEIVED_MESSAGES'
                elif arg == '-s' or arg == '--sent-messages':
                    command = 'SENT_MESSAGES'
                elif arg == '-S' or arg == '--send-message':
                    command = 'SEND_MESSAGE'
                elif arg == '-f' or arg == '--following':
                    command = 'FOLLOWING'
                elif arg == '-F' or arg == '--followers':
                    command = 'FOLLOWERS'
                elif arg == '--follow':
                    command = 'FOLLOW'
                elif arg == '--unfollow':
                    command = 'UNFOLLOW'
                elif arg == '--block':
                    command = 'BLOCK'
                elif arg == '--unblock':
                    command = 'UNBLOCK'
                elif arg == '-p' or arg == '--post':
                    command = 'POST'
                elif arg == '--share':
                    command = 'SHARE'
                elif arg == '--like':
                    command = 'LIKE'
                elif arg == '--unlike':
                    command = 'UNLIKE'
                elif arg == '-u' or arg == '--user':
                    command = 'USER'
                elif arg == '-U' or arg == '--user-timeline':
                    command = 'USER_TIMELINE'
                elif arg == '-h' or arg == '--help':
                    command = 'HELP'
                else:
                    return (None, None)
            elif command:
                params.append(arg)
            else:
                return (None, None)

        if len(params) < commands[command][0] or len(params) > commands[command][1]:
            return (None, None)

        return (command, params)


    def execCommand(self, cmd, args):
        if cmd == 'NETWORKS':
            self.networks()
        elif cmd == 'CREATE_ACCOUNT':
            self.createAccount(args[0], args[1])
        elif cmd == 'REGISTER_ACCOUNT':
            self.registerAccount(args[0], args[1])
        elif cmd == 'DELETE_ACCOUNT':
            self.deleteAccount(args[0], args[1])
        elif cmd == 'LIST_ACCOUNTS':
            self.listAccounts(None if len(args) == 0 else args[0])
        elif cmd == 'ME':
            self.me(args[0], args[1])
        elif cmd == 'TIMELINE':
            self.timeline(args[0], args[1], 0 if len(args) == 2 else args[2])
        elif cmd == 'RECEIVED_MESSAGES':
            self.receivedMessages(args[0], args[1])
        elif cmd == 'SENT_MESSAGES':
            self.sentMessages(args[0], args[1])
        elif cmd == 'SEND_MESSAGE':
            self.sendMessage(args[0], args[1], args[2], args[3])
        elif cmd == 'FOLLOWING':
            self.following(args[0], args[1])
        elif cmd == 'FOLLOWERS':
            self.followers(args[0], args[1])
        elif cmd == 'FOLLOW':
            self.follow(args[0], args[1], args[2])
        elif cmd == 'UNFOLLOW':
            self.unfollow(args[0], args[1], args[2])
        elif cmd == 'BLOCK':
            self.block(args[0], args[1], args[2])
        elif cmd == 'UNBLOCK':
            self.unblock(args[0], args[1], args[2])
        elif cmd == 'POST':
            self.post(args[0], args[1], args[2])
        elif cmd == 'SHARE':
            self.share(args[0], args[1], args[2])
        elif cmd == 'LIKE':
            self.like(args[0], args[1], args[2])
        elif cmd == 'UNLIKE':
            self.unlike(args[0], args[1], args[2])
        elif cmd == 'USER':
            self.user(args[0], args[1], args[2])
        elif cmd == 'USER_TIMELINE':
            self.userTimeline(args[0], args[1], args[2],  0 if len(args) == 3 else args[3])
        elif cmd == 'HELP':
            self.help()

    def networks(self):
        print 'Networks:'
        k = 1
        for network in Account.supportedNetworks():
            print '\t[{0}] {1} (Authentication: {2})'.format(k, network, Account.networkToAccount(network))
            k += 1


    def createAccount(self, network, name):
        account = Account.getAccount(network, name)
        am = AccountManager()

        if account and am.create(account):
            print 'Create {0} account {1} : OK'.format(network, name)
        else:
            print 'Create {0} account {1} : FAIL'.format(network, name)


    def registerAccount(self, network, name):
        account = Account.getAccount(network, name)
        am = AccountManager()

        if account:
            accountType = Account.networkToAccount(network)
            callback = None

            if accountType == 'OAuth':
                callback = self.enterOAuthVerifier
            elif accountType == 'UserPass':
                callback = self.enterUserPass

            if callback and am.register(account, callback):
                print 'Register {0} account {1} : OK'.format(network, name)
        else:
            print 'Register {0} account {1} : FAIL'.format(network, name)



    def deleteAccount(self, network, name):
        account = Account.getAccount(network, name)
        am = AccountManager()

        if account and am.remove(account):
            print 'Delete {0} account {1} : OK'.format(network, name)
        else:
            print 'Delete {0} account {1} : FAIL'.format(network, name)


    def listAccounts(self, network):
        am = AccountManager()
        accounts = am.getAll() if network is None else am.getAllByNetwork(network)

        print 'Account List:'

        if len(accounts) == 0:
            print 'Empty'
            return

        k = 1
        for account in accounts:
            print '\t[{0}] {1} account {2} [{3}]'.format(k, account.network, account.name, 'Registered' if account.isRegistered() else 'Not Registered')
            k += 1


    def me(self, network, name):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Me:'.format(network, name)
        user = controller.me()
        print '\n\t{0} (@{1}) {2}'.format(user.name.encode('utf-8'), user.screen_name, '' if user.description is None else '\n\t' + user.description.encode('utf-8'))
        print '\tLocation: {0}'.format(user.location.encode('utf-8'))
        print '\tFollowing: {0} Followers: {1} Tweets: {2} Favorites: {3}'.format(user.friends_count, user.followers_count, user.statuses_count, user.favourites_count)


    def timeline(self, network, name, limit):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Timeline:'.format(network, name)

        k = 1
        for tweet in controller.timeline(int(limit)):
            print '\n\t[{0}] {1} (@{2}) {3}{4} via {5}'.format(k, tweet.user.name.encode('utf-8'), tweet.user.screen_name, tweet.created_at,
                                                        '' if tweet.in_reply_to_screen_name is None else ' in reply to @' + tweet.in_reply_to_screen_name,
                                                        tweet.source.encode('utf-8'))
            print '\t\t{0}'.format(tweet.text.encode('utf-8'))
            print '\tID: {0} Retweets: {1} Favorites: {2}'.format(tweet.id, tweet.retweet_count, tweet.favorite_count)
            k += 1


    def receivedMessages(self, network, name):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Received Messages:'.format(network, name)

        k = 1
        for message in controller.receivedMessages():
            print '\n\t[{0}] {1} (@{2}) {3}'.format(k, message.sender.name.encode('utf-8'), message.sender.screen_name, message.created_at)
            print '\t\t{0}'.format(message.text.encode('utf-8'))
            k += 1


    def sentMessages(self, network, name):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Sent Messages:'.format(network, name)

        k = 1
        for message in controller.sentMessages():
            print '\n\t[{0}] {1} (@{2}) {3}'.format(k, message.recipient.name.encode('utf-8'), message.recipient.screen_name, message.created_at)
            print '\t\t{0}'.format(message.text.encode('utf-8'))
            k += 1


    def sendMessage(self, network, name, id, message):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        msg = controller.sendMessage(id, message)
        print '{0} account {1} Send Message: {2}'.format(network, name, 'Error' if msg is None else 'OK - ID: ' + msg.id_str)


    def following(self, network, name):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Following:'.format(network, name)

        k = 1
        for user in controller.following():
            print '\n\t[{0}] {1} (@{2}) {3}'.format(k, user.name.encode('utf-8'), user.screen_name, '' if user.description is None else '\n\t' + user.description.encode('utf-8'))
            print '\tLocation: {0}'.format(user.location.encode('utf-8'))
            print '\tFollowing: {0} Followers: {1} Tweets: {2} Favorites: {3}'.format(user.friends_count, user.followers_count, user.statuses_count, user.favourites_count)
            k += 1


    def followers(self, network, name):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} Followers:'.format(network, name)

        k = 1
        for user in controller.followers():
            print '\n\t[{0}] {1} (@{2}) {3}'.format(k, user.name.encode('utf-8'), user.screen_name, '' if user.description is None else '\n\t' + user.description.encode('utf-8'))
            print '\tLocation: {0}'.format(user.location.encode('utf-8'))
            print '\tFollowing: {0} Followers: {1} Tweets: {2} Favorites: {3}'.format(user.friends_count, user.followers_count, user.statuses_count, user.favourites_count)
            k += 1

    def follow(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        user = controller.follow(id)

        print '{0} account {1} Follow: {2}'.format(network, name, 'Error' if user is None else 'OK - ID: @' + user.screen_name)


    def unfollow(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        user = controller.unfollow(id)

        print '{0} account {1} Unfollow: {2}'.format(network, name, 'Error' if user is None else 'OK - ID: @' + user.screen_name)


    def block(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        user = controller.block(id)

        print '{0} account {1} Block: {2}'.format(network, name, 'Error' if user is None else 'OK - ID: @' + user.screen_name)


    def unblock(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        user = controller.unblock(id)

        print '{0} account {1} Unblock: {2}'.format(network, name, 'Error' if user is None else 'OK - ID: @' + user.screen_name)


    def post(self, network, name, message):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        tweet = controller.post(message)

        print '{0} account {1} Post: {2}'.format(network, name, 'Error' if tweet is None else 'OK - ID: ' + tweet.id_str)


    def share(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        tweet = controller.share(int(id))

        print '{0} account {1} Share: {2}'.format(network, name, 'Error' if tweet is None else 'OK - ID: ' + tweet.id_str)


    def like(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        tweet = controller.like(int(id))

        print '{0} account {1} Like: {2}'.format(network, name, 'Error' if tweet is None else 'OK - ID: ' + tweet.id_str)


    def unlike(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        tweet = controller.unlike(int(id))

        print '{0} account {1} Unlike: {2}'.format(network, name, 'Error' if tweet is None else 'OK - ID: ' + tweet.id_str)


    def user(self, network, name, id):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} User:'.format(network, name)
        user = controller.user(id)
        print '\n\t{0} (@{1}) {2}'.format(user.name.encode('utf-8'), user.screen_name, '' if user.description is None else '\n\t' + user.description.encode('utf-8'))
        print '\tLocation: {0}'.format(user.location.encode('utf-8'))
        print '\tFollowing: {0} Followers: {1} Tweets: {2} Favorites: {3}'.format(user.friends_count, user.followers_count, user.statuses_count, user.favourites_count)


    def userTimeline(self, network, name, id, limit):
        am = AccountManager()
        account = am.get(network, name)
        controller = account.controller()

        print '{0} account {1} User Timeline:'.format(network, name)

        k = 1
        for tweet in controller.userTimeline(id, int(limit)):
            print '\n\t[{0}] {1} (@{2}) {3}{4} via {5}'.format(k, tweet.user.name.encode('utf-8'), tweet.user.screen_name, tweet.created_at,
                                                        '' if tweet.in_reply_to_screen_name is None else ' in reply to @' + tweet.in_reply_to_screen_name,
                                                        tweet.source.encode('utf-8'))
            print '\t\t{0}'.format(tweet.text.encode('utf-8'))
            print '\tID: {0} Retweets: {1} Favorites: {2}'.format(tweet.id, tweet.retweet_count, tweet.favorite_count)
            k += 1


    def enterOAuthVerifier(self, url = None):
        if url:
            print 'URL: {0}'.format(url)

        return raw_input('Verifier:')


    def enterUserPass(self):
        user = raw_input('User:')
        password = raw_input('Pass:')

        return (user, password)


    def help(self):
        print '{0} {1} - {2}'.format(atributes.APPLICATION_NAME, atributes.APPLICATION_VERSION, atributes.APPLICATION_DESC)
        print '\n\tUsage: {0} <command> [param ...]'.format(sys.argv[0])
        print '\nCOMMANDS'
        print '\n\t -n --networks\t\t\t\t\t\t\tShow the social networks supported by the application'
        print '\n\t -c --create-account <network> <name>\t\t\t\tCreate a new social network account'
        print '\n\t -r --register-account <network> <name>\t\t\t\tRegister an existing account'
        print '\n\t -d --delete-account <network> <name>\t\t\t\tDelete an existing account'
        print '\n\t -l --list-accounts [network]\t\t\t\t\tList all accounts'
        print '\n\t -m --me <network> <name>\t\t\t\t\tShow information about your user for a registered account'
        print '\n\t -t --timeline <network> <name> [limit]\t\t\t\tShow the current timeline for a registered account'
        print '\n\t -R --received-messages <network> <name>\t\t\tShow the received messages for a registered account'
        print '\n\t -s --sent-messages <network> <name>\t\t\t\tShow the sent messages for a registered account'
        print '\n\t -S --send-message <network> <name> <user_id> <message>\t\tSend a message to an user for a registered account'
        print '\n\t -f --following <network> <name>\t\t\t\tShow the list of users followed by a registered account'
        print '\n\t -F --followers <network> <name>\t\t\t\tShow the list of users following a registered account'
        print '\n\t    --follow <network> <name> <user_id>\t\t\t\tFollow an user on registered account'
        print '\n\t    --unfollow <network> <name> <user_id>\t\t\tUnfollow an user on registered account'
        print '\n\t    --block <network> <name> <user_id>\t\t\t\tBlock an user on registered account'
        print '\n\t -p --post <network> <name> <message>\t\t\t\tPost a message on registered account'
        print '\n\t    --share <network> <name> <message_id>\t\t\tShare a message with followers on registered account'
        print '\n\t    --like <network> <name> <message_id>\t\t\tLike a message on registered account'
        print '\n\t    --unlike <network> <name> <message_id>\t\t\tUnlike a message on registered account'
        print '\n\t -u --user <network> <name> <user_id>\t\t\t\tShow information about user for a registered account'
        print '\n\t -U --user-timeline <network> <name> <user_id> [limit]\t\tShow the current user timeline for a registered account'
        print '\n\t -h --help\t\t\t\t\t\t\tShow this help message\n'
