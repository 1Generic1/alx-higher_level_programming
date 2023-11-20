#!/usr/bin/python3
"""
This script lists all cities from the database 
hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to the MySQL server and retrieves values
    from the states table where the name matches the provided state name.

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
    query = (
        "SELECT cities.id, cities.name, states.name FROM "
        "cities INNER JOIN states ON states.id=cities.state_id "
        "ORDER BY id ASC"
        )
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
list_cities(username, password, database)

