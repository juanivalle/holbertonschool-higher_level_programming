#!/usr/bin/python3
"""
    task 3
"""
import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=arg[1], passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
                   FROM states JOIN cities ON state_id=states.id \
                   WHERE states.name LIKE %s ORDER BY cities.id",(arg[4],))
    rows = cursor.fetchall()
    i = ""
    for row in rows:
        if (row != rows[0]):
            i += ", "
        i += row[0]
    print(i)
    cursor.close()
    db.close()
