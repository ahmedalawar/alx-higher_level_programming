#!/usr/bin/python3
""" Script that list all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # It gives us the ability to have multiple seperate working enviroments
    # throught the same connection to the dataase.
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # clean up process
    cur.close()
    db.close()
