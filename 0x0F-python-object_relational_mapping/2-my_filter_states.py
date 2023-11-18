#!/usr/bin/python3
"""
This script retrieves values from the states table
where the name matches the provided state name
"""

import MySQLdb
import sys

def search_states(username, password, database, search_name):
    """
    Connects to the MySQL server and retrieves values from the states table where the name matches the provided state name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        search_name (str): State name to search for.

    Returns:
        None
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd="Mysqlpassword1$$",
        db=database
        )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(search_name)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    print("Username:", username)
print("Password:", password)
print("Database:", database)
print("Search Name:", search_name)
