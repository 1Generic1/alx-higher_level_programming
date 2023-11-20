#!/usr/bin/python3
"""
This script lists all cities from the database
hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd="Mysqlpassword1$$",
                         db=database)
    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name FROM "
        "cities INNER JOIN states ON states.id=cities.state_id "
        "ORDER BY id ASC"
        )
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
