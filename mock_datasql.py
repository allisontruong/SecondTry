import sqlite3
import time
import datetime
import random


def create_table(dbInfo):
    """
    Create a table for our DB
    :param dbInfo: dbInfo
    :return: nothing
    """
    dbInfo['cur'].execute("""CREATE TABLE IF NOT EXISTS mock_data
         (id         INT,
         snumber    INT,
         sname      TEXT,
         city       TEXT,
         state      TEXT,
         postalCode TEXT,
         hprice     REAL)""")
    print("Done creating mock_data table")

def read_data(dbInfo):
    """
    Reads data from DB
    :param dbInfo:
    :return: nothing
    """
    dbInfo['cur'].execute("""SELECT * FROM mock_data""")
    data = dbInfo['cur'].fetchall()
    return data

def dynamic_data_entry(dbInfo, rec):
    """
    Dynamically enter information to table
    :param dbInfo: DB connection dict
    :return: nothing
    """
    unix = int(time.time())
    # datetime.datetime.fromtimestamp: takes a unix time
    # strtime: will convert to a string in any format
    date = datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")
    keyword = 'Python'
    value = random.randrange(0, 10) # random 0-10
    dbInfo['cur'].execute("""INSERT INTO mock_data
            (id, snumber, sname, city, state, postalCode, hprice)
            VALUES(?, ?, ?, ?, ?, ?, ?)""",
            rec)
    # Commit to DB
    #dbInfo['con'].commit()
    print("Inserting {}".format(rec))

def main():
    dbInfo = {} # db related info
    # Connect to DB
    dbInfo['con'] = sqlite3.connect('tutorial.db')
    # Create a cursor (interact with DB)
    dbInfo['cur'] = dbInfo['con'].cursor()
    # 1) Create a table
    #create_table(dbInfo)
    # 2) Insert data
    #data_entry(dbInfo)
    # for i in range(10):
    #     dynamic_data_entry(dbInfo)
    #     time.sleep(3)
    # 3) Read data
    #read_data(dbInfo)
    # 4) Delete data
    delete_data(dbInfo)

    # Clean
    dbInfo['cur'].close()
    dbInfo['con'].close()

if __name__ == '__main__':
    main()