## Working on SQL PLUS (Oracle)
### Common command
Logging
```
spool C:\path\file_name

// to stop record
spool off
```
Create table
```
create table table_name (
  col_1_name type,
  col_2_name type,
  ...,
  col_n_name type);
```
Alter table
```
```
Insert value
```
insert into table_name values(
  value_1,
  value_2,
  ...,
  value_n);
```
Update data
```
update table_name set a = 5 where c = 40;
```
Set special character using 'escape'
```
SELECT last_name FROM employees
WHERE job_id LIKE 'M_\_%' escape '\'
// output: job_id = MA_ABC, MC_XYZ
```
__________________________________________________________
### Formatting data when SELECT
Setting UPPERCASE, lowercase
```
// UPPERCASE
upper(col)
upper'king'

// lowercase
lower(col)

// UPPER first letter, the rest are lower
initcap(col)
```
Set null to specific value
```
nvl(col_name, 0)
// change null to zero (0)

SELECT nvl(price, 0) FROM products;
```
__________________________________________________________
### Substitution variables
Check define list
```
define

//Checking specific define
define col
```
Define new word
```
defind a = 10
```
Calling the defined word
```
SELECT * FROM abc
WHERE a = &a;
```
Undefine
```
undefine a
```
Prompt wait for user to pass value everytime
```
SELECT * FROM employees
WHERE id = &col1;
// command will wait for col1 value
// if no prompt, 'col1' already defined
```
Prompt wait for user to pass value and record to define
```
SELECT * FROM employees
WHERE id = &&col2;
// command will wait for col2 value, and if col2 is called again, it will not need user to pass value.
```
Undefine to removed the recorded value
```
undefine col2
```
__________________________________________________________
### Setting
Set line size, page size
```
show pagesize
set pagesize 120

show linesize
set linesize 60
```
