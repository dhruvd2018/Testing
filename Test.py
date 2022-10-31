#generate SQL inquiry
sql = "SELECT * FROM table WHERE id = %s" % (id) 
#connect to database
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test")
#execute SQL inquiry
cursor = db.cursor()
cursor.execute(sql)
#fetch results
results = cursor.fetchall()
#close connection
db.close()
#return results
return results

# Path: Test.py
#generate SQL inquiry
sql = "SELECT * FROM table WHERE id = %s" % (id) 
#connect to database
db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="test")
#execute SQL inquiry
cursor = db.cursor()
cursor.execute(sql)
#fetch results
results = cursor.fetchall()
#close connection
db.close()
#return results
return results  #this is the line that is causing the error 

