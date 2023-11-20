#!/usr/bin/python3
"""
This script retrieves values from the states table
where the name matches the provided state name
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd="Mysqlpassword1$$",
                         db=database)
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY %s")
    cursor.execute(query, sys.argv[4])
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
~              
