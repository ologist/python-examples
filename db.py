import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")

cursor = db.cursor()

cursor.execute("SELECT * from test")

for row in cursor.fetchall() :
 print row[0]
