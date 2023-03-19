#!/usr/bin/python3
"""
    task 2
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    arg = sys.argv
    db = MySQLdb.connect(host=host="localhost", port=3306, 
            user=arg[1],passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name like '{}' ORDER BY id ASC".format(arg[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
