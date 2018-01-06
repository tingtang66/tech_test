import os
from handlers.homepage import IndexHandler
from tornado.web import StaticFileHandler
route = []
route.append((
    r'/static/(.*)',
    StaticFileHandler,
    {'path': os.path.join(os.path.dirname(__file__), "static")}
))
route.append((r'/', IndexHandler))
