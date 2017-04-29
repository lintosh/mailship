#~ util package that would hold common functionalities and tools that all versions of the api would use
#(@: Name): "mailMorth"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence Protective Rights please edit and use it with all the care you can give

#this 

#import the user handlers
from user import Users
import connect
from classes import generateKey
from flask import session,request
#end all import

user=Users(__name__)# start user manager

def Authenticate(appName,Key):
	if user.isAuth(appName,Key,request.remote_addr)==True:

		print "Valid user"
		return {"Response":{"Header":{"version":1.0,"type":"aplication/json"},"User":{"clientKey":Key,"Auth":True,"status":200}}}#~ return a response

	else:
		print appName+" "+Key+" "+request.remote_addr
		print "Aww invalid user"
		return {"Response":{"Header":{"version":1.0,"type":"aplication/json"},"User":{"clientKey":Key,"Auth":False,"status":404}}}#~ return a response	


def checkSignature(appName):
	if user.isActive(appName,request.remote_addr)==True:
		return True
	else:
		return False


#authorize user key by validating an generate a response
def Auth(conn,appName,appKey):
		if checkSignature(appName) is not True:#~ not authenticated and register in the user base 
			from data import validateAuth#import the model package to handle checking of client authentication
			authenticate=validateAuth(conn,appName,appKey)
			# print "authenticate{}".format(authenticate)
			if authenticate==True:
				clientKey=generateKey(appKey)
				print "client generated key is "+clientKey
				print "Authenticated"
				user.add(appName,clientKey)#add to user queue
				session[appName]=clientKey #add to session queue
				return[clientKey,True] # ~generate clientAuth and return back to client

			else:
				return[404,False] # ~return error msg back to client

		else:#~ if already authenticated in the user base do this
			if checkSignature(appName)==True:
				print "User already Authenticated"
				return[user.get(appName)["key"],True] # ~generate clientAuth and return back to client
			else:
				print "Error Authenticating user"
				return[404,False] # ~return error msg back to client