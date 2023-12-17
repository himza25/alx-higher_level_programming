#!/usr/bin/python3
"""
This module contains a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    # Create and execute the query
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    .format(sys.argv[4])
    cur.execute(query)

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
