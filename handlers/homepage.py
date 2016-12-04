import os
from tornado.web import RequestHandler
from handlers import Env

class IndexHandler(RequestHandler):
    def get(self):
        host_ip = os.environ['HOST_IP']
        template = Env.get_template('index.j2')
        self.write(template.render(output=host_ip))

