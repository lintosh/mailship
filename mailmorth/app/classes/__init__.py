import hashlib
import base64
import datetime

def generateKey(ApiKey):#cleitnKey generator
	millis= datetime.datetime.now()# ~get time
	encodedKey=base64.b64encode(hashlib.sha1(bytes(ApiKey+str(millis))).digest())#encode user's authKey into base64 and hash
	#now Key is ready
	return encodedKey.split("=")[0].replace("/","$$")