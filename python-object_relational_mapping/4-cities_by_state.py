#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

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
    query = """SELECT cities.id, cities.name, states.name
                     FROM cities
                     INNER JOIN states ON cities.state_id = states.id"""
    
    mycursor.execute(query)

    rows = mycursor.fetchall()

    for x in mycursor:
        print(x)
