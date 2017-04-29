#~ version one of the mailMorth api which would hold all the functionalities of our version one
#(@: Name): "mailMorth"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence Protective Rights please edit and use it with all the care you can give

#import blueprint class

from flask_restplus import Resource
from api_version.utils import Auth,Authenticate
from views.connect import start as start
from flask import request




#----------------------------------------------------------------------------------
"""Accepts authKey as Key and appName as app from the clientA and produce a clientKey
	which would serve as an identity for clientA and must be returned on every request
"""
#----------------------------------------------------------------------------------

class connect(Resource):

	def get(self,app,Key):
		from db import DB#import connector for database
		conn=DB()		
		# return {"request":"success"}
		res=Auth(conn,app,Key)#authenticate user

		return {"Response":{"Header":{"version":1.0,"type":"aplication/json"},"User":{"clientKey":res[0],"Auth":res[1],"status":200}}}#~ return a response

#----------------------------------------------------------------------------------
#	end of client connection,authentication and key signing
#----------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
"""Connect with user's email clients e.g gmail,yahoo and all stuff
	the util files,methods and functions would be used to carry out some authentication processes
	at the same time handle email serving and connection
"""
#----------------------------------------------------------------------------------



class connectMail(Resource):
	#<string:app>/<string:clientKey>/<string:email>/<string:password>
	"""
	This class handles the connecting of a user to his email service provided using the imap functionality
	it takes three parameters which are clientKey, email address, and email password
	method:Post
	"""
	# def get(self,app,clientKey):
	# 	return Authenticate(app,clientKey)
	def post(self,app,clientKey):
		email=request.form["email"]
		password=request.form["password"]
		print "Authenticating..."
		return Authenticate(app,clientKey)
		# startService()

#----------------------------------------------------------------------------------
#	end of email client connection
#----------------------------------------------------------------------------------