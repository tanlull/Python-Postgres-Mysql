import psycopg2 as pg
def deleteData(id):
    try:
        conn = pg.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="postgres")
        cursor = conn.cursor()
        # Update single record now
        sql_delete_query = "Delete from source where id = %s"
        cursor.execute(sql_delete_query, (id,))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
    except (Exception, pg.Error) as error:
        print("Error in Delete operation", error)
    finally:
        # closing database conn.
        if (conn):
            cursor.close()
            conn.close()
            print("PostgreSQL conn is closed")

deleteData(10)