from uuid import uuid4
import tornado.web

class chatBasicHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        session = uuid4()
        self.render('basic.html', session=session)

class homeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        n = self.get_argument('n')
        u = self.get_argument('u')
        self.render('home.html', n=n, u=u)
