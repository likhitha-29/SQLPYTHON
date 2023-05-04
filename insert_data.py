import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database ='likhitha')
c=mydb.cursor()
z='insert into swap(id,name,salary) values(%s,%s,%s)'
a=(100,"ruks",10000)
c.execute(z,a)
mydb.commit()
print("Data inserted successfully")