#!/usr/bin/python3
"""
select a state matching state name searched
parameters: username, password, database, state name searched
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states\
        WHERE name LIKE '{}'\
        ORDER BY id ASC".format(argv[4])
    )
    rows = cur.fetchall()
    for row in rows:
        # To account for case insentivity search
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
