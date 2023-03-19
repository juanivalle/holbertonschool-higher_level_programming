#!/usr/bin/python3
"""comments"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    arg = sys.argv
    db = MySQLdb.connect(host=host="localhost", port=3306, 
            user=arg[1],passwd=arg[2], db=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
