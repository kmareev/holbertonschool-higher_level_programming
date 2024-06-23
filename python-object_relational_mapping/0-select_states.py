#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

# Connect to a the MySQL server
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

# Create a cursor object to interact with the DB
mycursor = db.cursor()

# Execute a query to retrieve all states sorted by ID in ASC order
mycursor.execute("SELECT * FROM states ORDER BY id")

# Fetch all the rows
rows = mycursor.fetchall()

# Print the results
for row in rows:
    print(row)
