import sqlite3
from sqlite3 import Error
from time import ctime

def sql_connect():
    try:
        con = sqlite3.connect('stock.db')
        return con
    except Error:
        print(Error)
 
def create_table(con, symbol):
    crs = con.cursor()
    crs.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+ symbol + "'")
    exist = int(crs.fetchone()[0])
    print(symbol + ' = ' + str(exist))
    if(exist == 0) :
        crs.execute("CREATE TABLE " + symbol + "(time,price,open,high,low,avg,lot,change,b1,b2,b3,b4,b5,b6,bl1,bl2,bl3,bl4,bl5,bl6,o1,o2,o3,o4,o5,o6,ol1,ol2,ol3,ol4,ol5,ol6,btotal,ototal)")
        con.commit()
    # else :
    #     print('Database exist!')

def insert_data(symbol, data):
    con = sql_connect()
    create_table(con, symbol)
    try : 
        crs = con.cursor()
        crs.execute('INSERT INTO '+ symbol +'(time,price,open,high,low,avg,lot,change,b1,b2,b3,b4,b5,b6,bl1,bl2,bl3,bl4,bl5,bl6,o1,o2,o3,o4,o5,o6,ol1,ol2,ol3,ol4,ol5,ol6,btotal,ototal) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data)
        con.commit()
        crs.close()
    except sqlite3.Error as error:
        with open('log.txt', 'a') as f:
            now = ctime()
            f.writelines( now + " - Fail to insert in database, " +  error + "\n")
    finally:
        if (con):
            con.close()



