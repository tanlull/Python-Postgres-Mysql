create table source(
id int4,
name text,
age int4,
gender text
)


truncate table source

insert into source values(1,'สมปอง',20,'male');
insert into source values(2,'สมชาย',22,'male');
insert into source values(3,'สมศรี',23,'female');
insert into source values(4,'สมสมร',24,'female');
commit;
rollback;

select * from source

SHOW client_encoding;
