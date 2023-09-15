#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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

    query = "SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states \
        ON states.id = cities.state_id \
        ORDER BY cities.id ASC;"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
