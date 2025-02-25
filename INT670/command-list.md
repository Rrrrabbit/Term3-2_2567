## Working on SQL PLUS (Oracle)
### Common command
Logging
```SQL
spool C:\path\file_name

-- to stop record
spool off
```
Login
```SQL
connect username/password
show user
```
List table on the schema
```SQL
SELECT * FROM tab;
```
Create table
```SQL
create table table_name (
  col_1_name type,
  col_2_name type,
  ...,
  col_n_name type);
```
Constraint
```SQL
create table table_name (
  col_1_name type contraint constraint_name not null PRIMARY KEY, -- or set PK last
  col_2_name type unique, --unique column level
  ...,
  col_n_name type,
  CONTSTRAINT con_name PRIMARY KEY (col1)
  CONTSTRAINT con_name FOREIGN KEY (col2) REFERENCES ref_table_name(ref_col_pk) ON DELETE [SET NULL|CASCADE]);

--unique table level (composite constraint)
create table abc (
  col1 number(5),
  col2 number(5),
  unique(col1, col2));
```
Show table properties
```SQL
desc table_name
```
Alter table
```SQL
alter table table_name add col_name type;
alter table table_name drop column col_name;
alter table table_name rename column old_name to new_name;
alter table table_name modify col_name type;

alter table table_name enable validate constraint constraint_name;
```
Insert value
```SQL
insert into table_name (col1, col2, ..., coln) values(
  value_1,
  value_2,
  ...,
  value_n);
```
Update value
```SQL
update table_name set a = 5 where c = 40;
```
Delete value
```SQL
delete from table_name;  --delete all data
delete from departments where dept_name = 'Finance';
```
Set special character using 'escape'
```SQL
SELECT last_name FROM employees
WHERE job_id LIKE 'M_\_%' escape "\";
-- output: job_id = MA_ABC, MC_XYZ
```
__________________________________________________________
### Datatype
Number
```SQL
> number(5,3)
-- a) 1.2345    => 1.235
-- b) 12.2345   => 12.235
-- c) 123.45    => value larger than specified precision
-- d) 12        => 12 (or 12.000)
-- e) 123.4     => value larger than specified precision
```
Variable length
```SQL
> varchar2(20)
-- if data is '1234567', the rest 13 index(?) are not preserved
```
DATE
```SQL
> date          => 08-FEB-25
> timestamp(6)  => 08-FEB-25 01.42.13.000000 PM

> interval year(2) to month
-- insert "interval '33' month"    => +02-09 (2 years 9 months)
-- insert "interval '330' month"   => +27-06 (27 years 6 months)

> interval day(2) to second(6)
-- insert "interval '2500' second"       => +00 00:41:40.000000 (41 mins 40 seconds)
-- insert "interval '25 2' day to hour"  => +25 02:00:00.000000
-- insert "interval '250 2' day to hour" => the leading precision of the interval is too small (because day(2))
```
__________________________________________________________
### Formatting data when SELECT
Setting UPPERCASE, lowercase
```SQL
-- UPPERCASE
upper(col)
upper'king'

-- lowercase
lower(col)

-- UPPER first letter, the rest are lower
initcap(col)
```
Set null to specific value
```SQL
nvl(col_name, 0)
-- change null to zero (0)

SELECT nvl(price, 0) FROM products;
```
__________________________________________________________
### Substitution variables
Check define list
```SQL
define

--Checking specific define
define col
```
Define new word
```SQL
defind a = 10
```
Calling the defined word
```SQL
SELECT * FROM abc
WHERE a = &a;
```
Undefine
```SQL
undefine a
```
Prompt wait for user to pass value everytime
```SQL
SELECT * FROM employees
WHERE id = &col1;
-- command will wait for col1 value
-- if no prompt, 'col1' already defined
```
Prompt wait for user to pass value and record to define
```SQL
SELECT * FROM employees
WHERE id = &&col2;
-- command will wait for col2 value, and if col2 is called again, it will not need user to pass value.
```
Undefine to removed the recorded value
```SQL
undefine col2
```
__________________________________________________________
### Drop
Drop
```SQL
drop table table_name
```
Restore
```SQL
flashback table table_name to before drop;
flashback table table_name to before drop rename to new_table_name;
```
__________________________________________________________
### Transaction
Save
```SQL
savepoint save_name
```
Restore
```SQL
rollback to save_name
```
__________________________________________________________
### Setting
Set line size, page size
```SQL
show pagesize
set pagesize 120

show linesize
set linesize 60
```
