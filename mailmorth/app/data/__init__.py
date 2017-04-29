#general model package please use with care
#don't tamper if you can't hamper
#dnt touch what you cant fix
#::-mail.intelijence (model package)




#let the job begin

def validateAuth(conn,User,Auth):#takes parameter as dbCursor for db related process
	"""Other parameters are the username and Auth to be validated """
	try:
		
		sqlStatement="""SELECT * FROM ijm_clientprograms WHERE IJM_Name='%s' AND IJM_Auth='%s'"""%(User,Auth)#sql statement
		
		fetchData=conn.execute(sqlStatement)
		rowData=conn.fetchall()
		if rowData:
			return True
		else:
			return False
	except Exception as e:
		print e
		return False
		
	
