#!/usr/bin/python3
"""list state by user input and prevent sql injection"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
