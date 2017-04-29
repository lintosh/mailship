#~ version one of the mailMorth api which would hold all the functionalities of our version one
#(@: Name): "mailMorth"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence Protective Rights please edit and use it with all the care you can give

#import blueprint class


from flask import Blueprint,request
from flask_restplus import Api, reqparse
from views import connect,connectMail

#end all import


#----------------------------------------------------------------------------------
#Create BluePrint and API
#----------------------------------------------------------------------------------
api_v1 = Blueprint('api_v1', __name__)#create a blueprint structure of the flask class
mailApi=Api(api_v1)#initialize the api class by passing the flask object to it
# cursor=mysql.connect()
#----------------------------------------------------------------------------------
#End all BluePrint
#----------------------------------------------------------------------------------

#start routin pages here


mailApi.add_resource(connect,"/start/<string:app>/<string:Key>")
mailApi.add_resource(connectMail,"/startService/<string:app>/<string:clientKey>")
		
	
