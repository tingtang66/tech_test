from tornado.web import RequestHandler
import subprocess

class IndexHandler(RequestHandler):
    def get(self):
        uri = self.request.uri
        self.render("index.html", output=uri)

