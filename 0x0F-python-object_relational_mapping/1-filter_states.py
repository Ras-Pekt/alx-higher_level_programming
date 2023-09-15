#!/usr/bin/python3
"""
lists all states with a name starting with upper N
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST,
                         user=MY_USER,
                         passwd=MY_PASSWD,
                         db=MY_DB)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
