#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
from tornado.options import options
import tornado.web

from settings import settings
from urls import url_patterns


class TornadoMain(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(
        	self, url_patterns, **settings)


def main():
    app = TornadoMain()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	print('Tornado serving on port: {}'.format(options.port))
	main()
	