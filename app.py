#-*-coding:utf-8-*-
import json
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
from uuid import uuid4
import MySQLdb
from handlers import *

class ChatHome(object):
    chatRegister = {}

    def register(self, newer):
        home = str(newer.get_argument('n'))
        if home in self.chatRegister:
            self.chatRegister[home].append(newer)
        else:
            self.chatRegister[home] = [newer]

        message = {
            'from': 'sys',
            'message': '%s has joined the chat room（%s）' % (str(newer.get_argument('u')), home)
        }
        self.callbackTrigger(home, message)


    def unregister(self, lefter):
        home = str(lefter.get_argument('n'))
        self.chatRegister[home].remove(lefter)
        if self.chatRegister[home]:
            message = {
                'from': 'sys',
                'message': '%s has left the chat room（%s）' % (str(lefter.get_argument('u')), home)
            }
            self.callbackTrigger(home, message)


    def callbackNews(self, sender, message):
        home = str(sender.get_argument('n'))
        user = str(sender.get_argument('u'))
        message = {
            'from': user,
            'message': message
        }
        self.callbackTrigger(home, message)


    def callbackTrigger(self, home, message):
        for callbacker in self.chatRegister[home]:
            callbacker.write_message(json.dumps(message))


class newChatStatus(tornado.websocket.WebSocketHandler):
    def open(self):
        n = str(self.get_argument('n'))
        self.write_message(json.dumps({'from':'sys', 'message':'welcome to the chat room（%s）' % n}))
        self.application.chathome.register(self)

    def on_close(self):
        self.application.chathome.unregister(self)

    def on_message(self, message):
        self.application.chathome.callbackNews(self, message)


class Application(tornado.web.Application):
    def __init__(self):
        self.chathome = ChatHome()

        handlers = [
            (r'/', chatBasicHandler),
            (r'/home/', homeHandler),
            (r'/newChatStatus/', newChatStatus),
        ]

        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
