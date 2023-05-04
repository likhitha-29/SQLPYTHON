import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="likhitha")
c=mydb.cursor()
f='select * from swap'
c.execute(f)
dis=c.fetchall()
for x in dis:
    print(x)