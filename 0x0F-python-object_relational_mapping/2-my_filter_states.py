#!/usr/bin/python3
"""Filter states by user input."""

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

    # Execute the query to select states with the name provided by the user
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))
    all_rows = cur.fetchall()

    # Print each state that matches the user input
    for one in all_rows:
        print(one)

    # Close the cursor and the connection
    cur.close()
    db.close()
