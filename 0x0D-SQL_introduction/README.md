# 0x0D. SQL - Introduction
Concepts learnt:
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions

## Tasks
### 0. List databases
Write a script that lists all databases of your MySQL server.
```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -h localhost -u root -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```
### 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
```bash
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -h localhost -u root -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -h localhost -u root -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -h localhost -u root -p
Enter password: 
guillaume@ubuntu:~/$ 
```
### 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
```bash
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -h localhost -u root -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -h localhost -u root -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -h localhost -u root -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```
### 3. List tables
Write a script that lists all the tables of a database in your MySQL server.

- The database name will be passed as argument of mysql command (in the following example: `mysql` is the name of the database)
```bash 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -h localhost -u root -D mysql -p 
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 
```
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 

## Resources
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
- [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
## More info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```
### Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
### Use “container-on-demand” to run MySQL
**In the container, credentials are root/root**

- Ask for container Ubuntu 20.04
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:
```bash
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -u root -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```
**In the container, credentials are root/root**