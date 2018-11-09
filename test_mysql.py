import crud_mysql as my 

my.connect()
#data_to_insert = (6, 'สมเจตน์', 26,'male')
#my.insert(data_to_insert)
#my.updateTable(6,10)
my.deleteData(6)
my.selectAll()
my.close()