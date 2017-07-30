from uuid import uuid4
import tornado.web

class chatBasicHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        session = uuid4()
        self.render('index.html', session=session)

class signinHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('signin.html')

class signupHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('signup.html')

class homeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        n = self.get_argument('n')
        u = self.get_argument('u')
        self.render('chat.html', n=n, u=u)
