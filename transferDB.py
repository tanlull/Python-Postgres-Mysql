import crud_postgres as pg 
import crud_mysql as my 

my.connect()
pg.connect()
#pg.deleteData(6);
print("----- Postgres data ----");
source_records = pg.selectAll()
print("-----  Mysql Before Transfer data -----");
my.selectAll()
for row in source_records:
    data_to_insert = (row[0],row[1],row[2],row[3])
    my.insert(data_to_insert)

print("-----  Mysql After Transfer data -----");
my.selectAll()

pg.close()
my.close()