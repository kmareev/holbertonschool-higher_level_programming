#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    mycursor = db.cursor()

    query = ("""SELECT * FROM states
                     WHERE BINARY NAME = '{}'
                     ORDER BY id ASC""".format(sys.argv[4]))

    mycursor.execute(query)
    rows = mycursor.fetchall()

    for row in rows:
        print(row)
