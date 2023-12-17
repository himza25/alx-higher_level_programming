#!/usr/bin/python3
"""Filter states by name"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()

    # Safe query execution
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))

    # Fetch and display the results
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
