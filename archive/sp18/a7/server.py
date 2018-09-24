#!/usr/bin/env python3

from tornado.ioloop import IOLoop
from tornado.process import task_id, fork_processes
from tornado.web import Application, RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello, I am ID {}\n'.format(task_id()))

class CrashHandler(RequestHandler):
    def get(self):
        self.write('Crashing ID {}!\n'.format(task_id()))
        IOLoop.current().stop()

if __name__ == '__main__':
    app = Application([
        (r'/', MainHandler),
        (r'/crash', CrashHandler),
    ])
    fork_processes(6)
    app.listen(8080 + task_id(), address='127.0.0.1')
    IOLoop.current().start()
