#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    loc = "localhost"
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    myDb = MySQLdb.connect(host=loc, user=user, passwd=pas, db=db, port=3306)
    cur = myDb.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    myDb.close()