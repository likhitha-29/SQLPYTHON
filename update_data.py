import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="likhitha")
c=mydb.cursor()
x='update swap set salary=salary+100 where id=101'
c.execute(x)
mydb.commit()