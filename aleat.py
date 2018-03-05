#!/usr/bin/python3

import webapp
import random

class myWebapp(webapp.webApp):

	def process(self,parsedRequest):
			num = random.randint(1,10000000)
			return ("200 OK", "<html><body><h1>It works!</h1><p><a href= http://localhost:1234/"+str(num)+
					">Dame otra</a></p></body></html>")

if __name__ == "__main__":
		myapp = myWebapp("localhost",1234)