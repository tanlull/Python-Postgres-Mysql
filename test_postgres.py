import crud_postgres as pg 

pg.connect()
pg.selectAll()
data_to_insert = (6, 'สมเจตน์', 26,'male')
pg.insert(data_to_insert)
#pg.updateTable(6,10)
#pg.deleteData(10)
pg.selectAll()
pg.close()