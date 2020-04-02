import tornado.web
import tornado.ioloop
import sys 
import os

class basicRequestHnadler(tornado.web.RequestHandler):
    def get(self):
        self.write("Served from"+ str(os.getpid()))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/basic', basicRequestHnadler)
    ])
    port = 8882
    if (sys.argv.__len__() > 1):
        port=sys.argv[1]
    app.listen(port)
    print("Application is ready and listening on port "+str(port))
    tornado.ioloop.IOLoop.current().start()