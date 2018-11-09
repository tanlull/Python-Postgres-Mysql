import psycopg2 as pg
def updateTable(id, newid):
    try:
        conn = pg.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="postgres")
        cursor = conn.cursor()
        sql_update = "Update source set id = %s where id = %s"""
        cursor.execute(sql_update, (newid,id))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
    except (Exception, pg.Error) as error:
        print("Error in update operation", error)
    finally:
        # closing database conn.
        if (conn):
            cursor.close()
            conn.close()
            print("PostgreSQL conn is closed")


updateTable(5,10)