import crud_postgres as pg 
import crud_mysql as my 

my.connect()
pg.connect()

#data_to_insert = (5, 'สมแบ๋ว', 25,'female')
#pg.insert(data_to_insert)
#data_to_insert = (6, 'สมเจตน์', 26,'male')
#pg.insert(data_to_insert)

print("-----  Mysql Before Transfer data -----");
maxID = my.selectMaxID()
print("MaxID={}".format(maxID))
print("----- Postgres data ----");
source_records = pg.selectByID(maxID)
print("----- Insert data ----");
for row in source_records:
    data_to_insert = (row[0],row[1],row[2],row[3])
    my.insert(data_to_insert)

print("-----  Mysql After Transfer data -----");
my.selectAll()

pg.close()
my.close()