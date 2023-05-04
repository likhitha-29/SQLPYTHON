import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database="likhitha")
c=mydb.cursor()
t='create table swap(id integer(4),name varchar(30),salary integer(10))'
c.execute(t)