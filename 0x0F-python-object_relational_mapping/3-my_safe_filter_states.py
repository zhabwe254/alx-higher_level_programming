#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, but safe from MySQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (state_name,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
