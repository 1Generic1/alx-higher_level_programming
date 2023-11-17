#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.

Usage: ./list_states.py <username> <password> <database>
"""


import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to the MySQL server and retrieves a list of states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

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
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
