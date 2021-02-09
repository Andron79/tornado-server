from abc import ABC
import asyncio
from tornado.ioloop import IOLoop

import tornado.web
import tornado.websocket

from tornado.options import define, options

define("port", default=8888, type=int)


class WebSocketHandler(tornado.websocket.WebSocketHandler, ABC):
    def check_origin(self, origin):
        return True

    def open(self):
        print("New client connected")
        self.write_message("You are connected")

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("Client disconnected")


app = tornado.web.Application([
    (r'/', WebSocketHandler),
])

if __name__ == '__main__':
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    # IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    # io_loop = IOLoop.current()
    # asyncio.set_event_loop(io_loop.asyncio_loop)
    #
    # io_loop.start()
