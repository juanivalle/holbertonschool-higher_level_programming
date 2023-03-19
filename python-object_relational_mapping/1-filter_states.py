#!/usr/bin/python3
""" task 1 """


if __name__ == "__main__":
    import sys
    import MySQLdb
    arg = sys.argv
    db = MySQLdb.connect(host=host="localhost", port=3306, 
            user=arg[1],passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
