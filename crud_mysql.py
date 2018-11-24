import MySQLdb as mysql

conn = {};
cursor = {};

def connect():
   global conn,cursor
   try:
       conn = mysql.connect("localhost","root","","test" )
       conn.set_character_set('utf8')
       cursor = conn.cursor()
       cursor.execute('SET NAMES utf8;')
       cursor.execute('SET CHARACTER SET utf8;')
       cursor.execute('SET character_set_connection=utf8;')
       return True
   except (Exception, mysql.Error) as error:
       print("Error ", error)
       return False

def close():
    global conn,cursor
    if(conn):
        cursor.close()
        conn.close()
        print("----  MySQL Closed connection --")

def selectAll():
    global conn,cursor
    try:
        sql = "select * from target"
        cursor.execute(sql)
        records = cursor.fetchall() 
        for row in records:
            print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3])) 
        return records
    except (Exception, mysql.Error) as error :
        print ("Error while fetching data from Mysql.", error)

def selectMaxID():
    global conn,cursor
    try:
        sql = "select COALESCE(max(id),0) from target"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            return row
    except (Exception, mysql.Error) as error :
        print ("Error while fetching data from Mysql.", error)

def insert(data_to_insert):
    global conn,cursor
    try:
        insert_sql = "insert into target values(%s,%s,%s,%s)"
        #data_to_insert = (5, 'สมเจตน์', 25,'male')
        cursor.execute(insert_sql, data_to_insert)
        conn.commit()
        count = cursor.rowcount
    except (Exception, mysql.Error) as error :
        print ("Error while fetching data from Mysql.", error)

def updateTable(id, newid):
    global conn,cursor
    try:
        sql_update = "Update target set id = %s where id = %s"""
        cursor.execute(sql_update, (newid,id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
    except (Exception, mysql.Error) as error:
        print("Error in update operation", error)

def deleteData(id):
    global conn,cursor
    try:
        cursor = conn.cursor()
        sql_delete_query = "Delete from target where id = %s"
        cursor.execute(sql_delete_query, (id,))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
    except (Exception, mysql.Error) as error:
        print("Error in Delete operation", error)
