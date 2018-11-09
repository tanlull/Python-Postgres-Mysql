import psycopg2 as pg

conn = {};
cursor = {};

def connect():
    global conn,cursor
    try:
        conn = pg.connect(host="127.0.0.1",database="postgres", user="postgres", password="postgres")
        cursor = conn.cursor()
        return True 
    except:
        return False

def close():
    global conn,cursor
    if(conn):
        cursor.close()
        conn.close()
        print("---- Postgres Closed connection --")

def selectAll():
    global conn,cursor
    try:
        sql = "select * from source"
        cursor.execute(sql)
        records = cursor.fetchall() 
        for row in records:
            print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3])) 
        return records
    except (Exception, pg.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

def selectByID(id):
    global conn,cursor
    try:
        sql = "select * from source where id >%s"
        cursor.execute(sql,(id,))
        records = cursor.fetchall() 
        for row in records:
            print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3])) 
        return records
    except (Exception, pg.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

def insert(data_to_insert):
    global conn,cursor
    try:
        insert_sql = "insert into source values(%s,%s,%s,%s)"
        #data_to_insert = (5, 'สมเจตน์', 25,'male')
        cursor.execute(insert_sql, data_to_insert)
        conn.commit()
        count = cursor.rowcount
    except (Exception, pg.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)

def updateTable(id, newid):
    global conn,cursor
    try:
        sql_update = "Update source set id = %s where id = %s"""
        cursor.execute(sql_update, (newid,id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
    except (Exception, pg.Error) as error:
        print("Error in update operation", error)

def deleteData(id):
    global conn,cursor
    try:
        cursor = conn.cursor()
        sql_delete_query = "Delete from source where id = %s"
        cursor.execute(sql_delete_query, (id,))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
    except (Exception, pg.Error) as error:
        print("Error in Delete operation", error)


# Programming Part
#connect()
#data_to_insert = (6, 'สมเจตน์', 26,'male')
#insert(data_to_insert)
#updateTable(6,10)
#deleteData(10)
#selectAll()
#close()