import psycopg2 as pg
try:
   conn = pg.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="postgres")
   cursor = conn.cursor()
   insert_sql = "insert into source values(%s,%s,%s,%s)"
   data_to_insert = (5, 'สมเจตน์', 25,'male')
   cursor.execute(insert_sql, data_to_insert)
   conn.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into source table")
except (Exception, pg.Error) as error :
    if(conn):
        print("Failed to insert record into source table", error)
finally:
    #closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")