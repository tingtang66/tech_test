import os
from tornado.web import RequestHandler
from handlers import Env
from subprocess import check_output

class IndexHandler(RequestHandler):
    def get(self):
        host_ip = check_output(['curl', 'http://169.254.169.254/latest/meta-data/public-ipv4'])
        template = Env.get_template('index.j2')
        self.write(template.render(output=host_ip))

