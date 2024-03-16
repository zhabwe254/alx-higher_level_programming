#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
where the name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (state_name,))
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
