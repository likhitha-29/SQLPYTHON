import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Likhitha@29',database ='likhitha')
c=mydb.cursor()
z='insert into swap(id,name,salary) values(%s,%s,%s)'
a=[(101,"liks",20000),(102,"pari",3000)]
c.executemany(z,a)
mydb.commit()
print("Data inserted successfully")