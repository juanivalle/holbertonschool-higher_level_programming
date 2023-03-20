#!/usr/bin/python3
""" Task 4 """
import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=arg[1], passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
