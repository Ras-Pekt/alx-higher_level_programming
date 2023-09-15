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
    state_name = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST,
                         user=MY_USER,
                         passwd=MY_PASSWD,
                         db=MY_DB)

    cursor = db.cursor()

    query = "SELECT cities.name \
        FROM cities \
        JOIN states \
        ON states.id = cities.state_id \
        WHERE states.name=%s \
        ORDER BY cities.id ASC;"

    cursor.execute(query, (state_name, ))
    rows = cursor.fetchall()

    str_list = []
    for row in rows:
        str_list.append(row[0])

    print(", ".join(str_list))
