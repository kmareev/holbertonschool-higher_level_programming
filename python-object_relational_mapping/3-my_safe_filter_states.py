#!/usr/bin/python3
"""Module with the same function as 2-my_filter_states however,
this one is safe from MySQL injections!"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Input Sanitization to prevent MySQl injections
    for av in sys.argv:
        if av.count(";") > 0:
            exit()

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    mycursor = db.cursor()

    query = """SELECT * FROM states
                WHERE BINARY NAME = '{}'
                ORDER BY id ASC""".format(sys.argv[4])

    mycursor.execute(query)

    rows = mycursor.fetchall()

    for x in mycursor:
        print(x)
    