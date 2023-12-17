#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Unpack command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Create the SQL query string
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
