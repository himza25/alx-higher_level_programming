#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()

    # Execute the query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)

    # Fetch and print all rows from the query's result
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the connection
    cur.close()
    db.close()
