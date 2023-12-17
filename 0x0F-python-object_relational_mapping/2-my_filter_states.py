#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    # Create and execute the query
    # Use format() for creating the SQL query with the user input
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)

    # Fetch and display the results
    for row in cur.fetchall():
        print(row)

    # Close all cursors and databases
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
