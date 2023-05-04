import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="likhitha")
c=mydb.cursor()
f='delete from swap where id=100'
c.execute(f)
mydb.commit()