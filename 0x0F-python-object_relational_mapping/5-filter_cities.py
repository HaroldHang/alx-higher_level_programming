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
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    myDb.close()
