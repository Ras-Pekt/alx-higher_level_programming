#!/usr/bin/python3
"""
a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument,
and is safe from MySQL injections!
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASSWD = sys.argv[2]
    MY_DB = sys.argv[3]
    user_arg = sys.argv[4]

    db = MySQLdb.connect(host=MY_HOST,
                         user=MY_USER,
                         passwd=MY_PASSWD,
                         db=MY_DB)

    cursor = db.cursor()

    query = "SELECT * \
        FROM states \
        WHERE name \
        LIKE BINARY %s \
        ORDER BY id ASC;"

    cursor.execute(query, (f"{user_arg}",))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
