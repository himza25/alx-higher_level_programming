#!/usr/bin/python3
"""Filter states script that lists all states with a name starting with N."""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()

    # Execute the query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    all_rows = cur.fetchall()

    # Print each state that starts with 'N'
    for one in all_rows:
        print(one)

    # Close the cursor and the connection
    cur.close()
    db.close()
