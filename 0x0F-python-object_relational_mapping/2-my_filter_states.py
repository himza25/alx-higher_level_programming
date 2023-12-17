#!/usr/bin/python3
"""Filter states by user input"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()

    # Format the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(query.format(argv[4]))

    # Fetch and print all matching rows
    all_rows = cur.fetchall()
    for one in all_rows:
        if one[1] == argv[4]:
            print(one)

    # Close the cursor and the connection
    cur.close()
    db.close()
