import psycopg2 as pg
try:
    #Database Connection 
   conn = pg.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="postgres")
   cursor = conn.cursor()

   #SQL Query
   sql = "select * from source"
   cursor.execute(sql)
   records = cursor.fetchall() 
   print("Query=",sql)
   #Print data
   print("---- Print output -----")
   for row in records:
       print ("Id = {0} , Name = {1}, Age  = {2}, Gender  = {3}".format(row[0],row[1],row[2],row[3])) 
except (Exception, pg.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(conn):
        cursor.close()
        conn.close()
        print("----  closed connection --")