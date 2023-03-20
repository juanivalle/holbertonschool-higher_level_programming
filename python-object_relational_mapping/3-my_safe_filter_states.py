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
    cursor.execute("SELECT * FROM states"
                   "WHERE name LIKE %s ORDER BY id ASC".format(arg[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()