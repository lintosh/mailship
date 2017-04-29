#----------------------------------------------------------------------------------
# Describe project
#----------------------------------------------------------------------------------

#(@: Name): "mailMorth"

#(@:Description): "email Management, and automation api code"

#(@:Author): "inteliJence development team"

#under the license of Apache License 2.0 and intelijence Protective Rights please edit and use it with all the care you can give

#(@:App-Type): "Api (Restfull & RestLess)"

#(@:Language): "Python"

#(@:Language Compiler): "python 2.9"

#(@:Framework): "Flask"

#(@:Required-Modules): "Base64, PassLib, Flask, Flask_restPlus, Flask SQL Alchemy, Flask_MYSQL, Flask_Mail, Flask_Socket, Imaplib, python 2.9, email, html5lib, Jinja, Flask_Sijax, Flask_Admin, Flask_Login, flask-httpAuth **more to come**"

#wow if you are done with the above
#and
#you get it
#you are on the right track
#boom!!!!!!!! now lets start the job

#import the flask framework and all it's modules like the flask_restful and api's methods
#import all classes used in routing from the classes package/directory to access all api handlers

#----------------------------------------------------------------------------------
#	end Description
#----------------------------------------------------------------------------------

from api_version.v1 import mailApi,api_v1#~ import version1 of the api methods
from flask import Flask
from db import mysql#import connector for database



#----------------------------------------------------------------------------------
#initialize the classes and all resources to be used for the functioning of the api
#----------------------------------------------------------------------------------
mailMorth=Flask(__name__)
mailMorth.config["ERROR_404_HELP"]=False
# mailApi=Api(mailMorth)#initialize the api class by passing the flask object to it
mailMorth.secret_key='t!C|<@'
#----------------------------------------------------------------------------------
#	end initialize all required values
#----------------------------------------------------------------------------------

#-----------------------------------------
#	DbConnections is done here
#------------------------------------------
#db connection tooling
mailMorth.config['MYSQL_DATABASE_HOST']='localhost'#configure database host
mailMorth.config['MYSQL_DATABASE_DB']='IJM_api'#configure database name
mailMorth.config['MYSQL_DATABASE_PASSWORD']=''#CONFIGURE PASSWORD
mailMorth.config['MYSQL_DATABASE_USER']='root'
mysql.init_app(mailMorth)#initialize mysql to values set in app.config

#------------------------------------
#	End of connections
#------------------------------------

#------------------------------------------------------
#|||||||||||||||||||||||||||||||||||||||||||||||||||||
#routing blueprints starts now
mailMorth.register_blueprint(api_v1, url_prefix='/v1')
#end of route
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#----------------------------------------------------------

# @mailMorth.route("/start/<string:app>/<string:Key>")
# def loadPage():
	

#start server
if __name__ == '__main__':
	mailMorth.run(port=2020,debug=True)


