import tornado.web # will our request handler (the handler thar receive rquest from http protocole) 

import tornado.ioloop # the theard listening for our waiting for our result, waiting for request
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World this is a python command executed from the backend.")


class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
       num = self.get_argument("num")
       if (num.isdigit()):
          r = "odd" if int(num) % 2 else "even"
          self.write(f"The integer {num} is {r}")
       else:
          self.write(f"{num} is not a valid integer.")  
    # query to test http://localhost:8882/isEven?num=1 

class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits)) 
        
class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r")
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully."}))
        
class uploadImgHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    def post(self):
        files = self.request.files["fileImage"]
        print(files)
        # i want to write the file in the backend
        for f in files:
            # here will open the folder when we want to ut the data
            fh = open(f"img/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8882/img/{f.filename}")
    

if __name__ == "__main__":
    app = tornado.web.Application([ 
        (r"/", uploadImgHandler),
        (r"/isEven", queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler),
        (r"/list", listRequestHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'img'}) #The regex .* means "zero or more of any character,”
        # 'path': 'img' :folder img 
    ])
    
    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()