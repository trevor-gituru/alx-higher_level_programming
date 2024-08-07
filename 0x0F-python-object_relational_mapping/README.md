# 0x0F. Python - Object-relational mapping
Concepts learnt:
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment
## Background context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.
## Tasks
### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
### 1. Filter states
Write a script that lists all states with a name starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (no argument validation needed)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```
### 3. SQL Injection...
Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?
```bash
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
```
What? Empty?

Yes, it’s an [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where name matches the argument. But this time, write one that is safe from MySQL injections!

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$
``` 
**No test cases needed**
### 4. Cities by states
Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 5. All cities by state
Write a script that takes in the name of a `state` as an argument and lists all cities of that `state`, using the database `hbtn_0e_4_usa`

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
- You must use the module `MySQLdb` (import `MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port `3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$
``` 
**No test cases needed**
### 6. First state model
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

- `State` class:
    * inherits from `Base` [Tips](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)
    * links to the MySQL table `states`
    * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- You must use the module `SQLAlchemy`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- **WARNING:** all classes who inherit from Base must be imported before calling `Base.metadata.create_all(engine)`
```bash
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
```
```bash
guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 7. All states via SQLAlchemy
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - from `model_state` import `Base`, `State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -u root -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 8. First state
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a `MySQL` server running on `localhost` at port `3306`
- The state you display must be the first in `states.id`
- You are not allowed to fetch all `states` from the database before displaying the result
- The results must be displayed as they are in the example below
- If the table `states` is empty, print `Nothing` followed by a new line
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 9. Contains `a`
Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 10. Get a state
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name`, `state name to search` (SQL injection free)
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You can assume you have one record with the state name to search
- Results must display the `states.id`
- If no state has the name you searched for, display `Not found`
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 11. Add a new state
Write a script that adds the `State` object `“Louisiana”` to the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Print the new `states.id` after creation
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 12. Update a state
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Change the name of the `State` where `id = 2` to `New Mexico`
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 13. Delete states
Write a script that deletes all `State` objects with a `name` containing the letter `a` from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

- `City` class:
    * inherits from `Base` (imported from `model_state`)
    * links to the MySQL table `cities`
    * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute `name` that represents a column of a string of 128 characters and can’t be null
    * class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
- You must use the module `SQLAlchemy`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `cities.id`
- Results must be display as they are in the example below `(<state name>: (<city id>) <city name>)`
- Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/0x0F$ 
```
**No test cases needed**
## More Info
### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
### Install MySQLdb module version 2.0.x
For installing `MySQLdb`, you need to have `MySQL` installed: 
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
### Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
Also, you can have this warning message:
```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters) 
``` 
You can ignore it.


## Resources
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/cleanup.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#configuring-delete-delete-orphan-cascade)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL,but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)