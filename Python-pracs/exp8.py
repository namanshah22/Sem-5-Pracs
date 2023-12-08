import mysql.connector
connecting=mysql.connector.connect(host="localhost",user="root",password="naman@22")
connector=connecting.cursor()
# create database
#connector.execute("create database naman")
connector.execute("use naman")
# create table
#connector.execute("create table student(id int(5),name varchar(25))")
# insert values
#connector.execute("INSERT INTO student(id,name) VALUES(3,'rohit')")
#connector.execute("INSERT INTO student(id,name) VALUES(4,'mohit'),(7,'meet')")
#connecting.commit()
# delete
#connector.execute("DELETE from student where name='mohit';")
#connecting.commit()
# select
res=connector.execute("select * from student")
for row in res:
    print(row)

#print(res)