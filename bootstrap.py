#! /usr/bin/python
# -*- code:utf-8 -*-
import sys
from os.path import join, dirname
from tornado.web import Application
from tornado.ioloop import IOLoop
from route import route

settings = {
    'static_path': join(dirname(__file__), 'static'),
    'template_path': join(dirname(__file__), 'template')
}

if __name__ == '__main__':
    Application(route, debug=True, **settings).listen(sys.argv[1])
    IOLoop.instance().start()
