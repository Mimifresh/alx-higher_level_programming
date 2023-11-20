#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    conectt = MySQLdb.connect(host="localhost", port=3306,
                              user=mysql_username, passwd=mysql_password,
                              db=database_name, charset="utf8")
    cr = conectt.cursor()
    cr.execute("SELECT * FROM states ORDER BY states.id")
    resut = cr.fetchall()
    for r in resut:
        print(r)

    cr.close()
    conectt.close()
