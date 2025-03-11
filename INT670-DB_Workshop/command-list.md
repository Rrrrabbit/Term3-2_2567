## Working on SQL PLUS (Oracle)
### Common command
Logging - บันทึกข้อมูล history
```SQL
spool C:\path\file_name

-- to stop record
spool off
```
Login - เข้าสู่ระบบ
```SQL
connect username/password
show user
```
List table on the schema - แสดงตารางทั้งหมด
```SQL
SELECT * FROM tab;
```
Create table - สร้างตาราง
```SQL
create table table_name (
  col_1_name type,
  col_2_name type,
  ...,
  col_n_name type);
```
Constraint - ข้อจำกัด ข้อบังคับ
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
Synonym for more convenient calling
```SQL
create synonym hrdept for hr.departments;
SELECT * FROM hrdept;
```
__________________________________________________________
### Datatype
Number
```SQL
> number(5,3)
-- a) 1.2345    => 1.235
-- b) 12.2345   => 12.235
-- c) 123.45    => ERROR: value larger than specified precision
-- d) 12        => 12 (or 12.000)
-- e) 123.4     => ERROR: value larger than specified precision
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
-- insert "interval '250 2' day to hour" => ERROR: the leading precision of the interval is too small (because day(2))
```
__________________________________________________________
### SQL Functions (Formatting data when SELECT)
Setting UPPERCASE, lowercase - ตัวอักษรพิมพ์เล็ก พิมพ์ใหญ่
```SQL
-- UPPERCASE
upper(col)
upper'king'

-- lowercase
lower(col)

-- UPPER first letter, the rest are lower
initcap(col)
```
Set null to specific value - เปลี่ยนการแสดงค่า null
```SQL
nvl(col_name, 0)
-- change null to zero (0)

SELECT nvl(price, 0) FROM products;
```
SUBSTRING(string, start_position, length) - ตัดข้อความ
```SQL
> substr('SIT KMUTT', 1, 2)   =>  'SI'
> substr('SIT KMUTT', 3, 3)   =>  'T K'
> substr('SIT KMUTT', -2, 3)  =>  'TT'
> substr('SIT KMUTT', 1)      =>  'SIT KMUTT'
> substr('SIT KMUTT', 8)      =>  'TT'
```
INSTR(string, character(s), start_position, nth character) - หาตำแหน่งตัวอักษร
```SQL
> instr('SIT KMUTT', 'I', 1, 1)   =>  2  (finding the 1st 'I' starting from the 1st character = 1st 'I' is at 2nd char)
> instr('SIT KMUTT', 'I', 3, 1)   =>  0  (0 = couldn't find the character)
> instr('SIT KMUTT', 'I', -3, 1)  =>  2
> instr('SIT KMUTT', 'T', -3, 1)  =>  3
> instr('SIT KMUTT', 'T', -1, 2)  =>  8
> instr('SIT KMUTT', 'T')         =>  3
```
Left/Right padding - เติมฝั่งซ้ายขวา
```SQL
select lpad(last_name, 10, '%') from employees;
-- o/p
%%%%%%Abel
%%%%Davies
%%%De Haan

select rpad(salary, 7, '*') from employees;
-- o/p
4400***
13000**
6000***
```
Trimming - ตัดหัวท้ายข้อความ
```SQL
> trim(leadingg 'S' from 'SIT KMUTT')      =>  'IT KMUTT'
> trim(leadingg 'S' from 'SIT SSKMUTTSS')  =>  'IT SSKMUTTSS'
> trim(both 'S' from 'SIT SSKMUTTSS')      =>  'IT SSKMUTT'
> trim(both 'SI' from 'SIT SSKMUTTSS')     =>  ERROR: trim set should have only one character
> rtrim('SIT SSKMUTTSSISI', 'SI')          =>  'SIT SSKMUTT'
> ltrim('SIT SSKMUTTIIISSISI', 'SI')       =>  'T SSKMUTTIIISSISI'
```
Replacing character(s)
```SQL
> replace('KMKKKMTKKTKK', 'K', 'L')   =>  'LMLLLUTLLTLL'
> replace('KMKKKMTKKTKK', 'KM', 'L')  =>  'LKKKUTKKTKK'
> replace('JACk and JUE', 'J')        =>  'ACK and UE'
```
Number function
```SQL
> round(50.567, 2)    =>  50.57
> round(50.567, -1)   =>  50
> round(550.567, -2)  =>  600
> round(50.567)       =>  51
> round(555.567, -2)  =>  600
> round(555.567, -1)  =>  550

> trunc(50.567, 2)    =>  50.56
> trunc(50.567, -1)   =>  50
> trunc(550.567, -2)  =>  500
> trunc(555.567, -2)  =>  500

> mod(1600, 300)  =>  100
```
Date function
```SQL
select hire_date from employees;
-- o/p
03-JAN-90
07-FEB-99
07-JUN-94

select to_char(hire_date, 'DD-MON-RRRR HH:MI:SS') from employees;
-- o/p
03-JAN-1990 12:00:00
07-FEB-1999 12:00:00
07-JUN-1994 12:00:00

select to_char(hire_date, 'DD-MON-RRRR HH:MI:SS AM') from employees;
-- o/p
03-JAN-1990 12:00:00 AM
07-FEB-1999 12:00:00 AM
07-JUN-1994 12:00:00 AM

> to_char(to_date('8-MAR-2025')+1, 'DD-MON-RRRR HH:MI:SS AM')       =>  09-MAR-2025 12:00:00 AM
> to_char(to_date('8-MAR-2025')+(3/24), 'DD-MON-RRRR HH:MI:SS AM')  =>  08-MAR-2025 03:00:00 AM

> months_between('01-SEP-95', '11-JAN-94')  => 19.6774194
> add_months('31-JAN-96', 1)                => '29-FEB-96'
> next_day('01-SEP-95', 'FRIDAY')           => '08-SEP-95'
> last_day('01-FEB-95')                     => '28-FEB-95'

month: date 1-15 round up / date 16-31 round down
year: month 1-6 round up / month 7-12 round down
> round(to_date('25-JUL-03'), 'month')  =>  '01-AUG-03'
> round(to_date('25-JUL-03'), 'year')   =>  '01-JAN-04'
> trunc(to_date('25-JUL-03'), 'month')  =>  '01-JUL-03'
> trunc(to_date('25-JUL-03'), 'year')   =>  '01-JAN-03'

> round(to_date('15-MAR-25'), 'month')  =>  '01-MAR-25'
> round(to_date('16-MAR-25'), 'month')  =>  '01-APR-25'
> round(to_date('16-MAY-25'), 'year')   =>  '01-JAN-25'
> round(to_date('16-JUN-25'), 'year')   =>  '01-JAN-25'
> round(to_date('16-JUL-25'), 'year')   =>  '01-JAN-26'
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
define a = 10
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
### Administration / Privileges
Create role
```SQL
create role student;
grant alter session to student;
grant create session to student;
grant create procedure to student; 
grant create trigger to student;
grant create type to student;
grant query rewrite to student;
grant create any index to student;
grant create public synonym to student;
```
Create user
```SQL
create user username01 identified by password01
default tablespace users
quota 10m on users  -- sete quota for each user
grant create table, create view, create sequence, create synonym to username01;
grant connect to username01;
grant role_name to username01;
```
__________________________________________________________
### Transaction
Save
```SQL
savepoint save_name
```
Commit to save changes
```SQL
commit
```
Restore or rollback to revert changes
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
