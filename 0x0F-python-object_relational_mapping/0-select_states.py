#!/usr/bin/python3
"""lists all states in a database"""

if __name__ == "__main__":
    import MySQLdb
    import sys


    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASSWD, db=MY_DB)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
