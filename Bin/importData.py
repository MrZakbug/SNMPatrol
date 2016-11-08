import sqlite3
import random
from time import strftime, sleep

files = ['MIB16', 'MIB2', 'MIB3', 'MIB4', 'MIB5',
         'MIB6', 'MIB7', 'MIB8', 'MIB9', 'MIB10',
         'MIB11', 'MIB12', 'MIB13', 'MIB14', 'MIB15',
         'MIB16', 'MIB17', 'MIB18', 'MIB19', 'MIB20', ]


def list_of_value_mib():
    # Read file and create a list of MIBs of value
    # Read file with MIBs we want
    value_mibs_path = 'required\\neededMIB.txt'
    read_file = open(value_mibs_path, 'r')
    # Create a list
    value_mibs = []
    for line in read_file:
        value_mibs.append(line.rstrip('\n'))
    read_file.close()
    return value_mibs


db = sqlite3.connect('SNMPatrol.db')  # Create a database


def insert_data():
    # load and insert data
    mib_trap = 'required\\' + random.choice(files) + '.txt'
    read_file = open(mib_trap, 'r')
    for line in read_file:                               # IF-MIB::ifInOctets.1 = Counter32: 5217689
        file_line = line.split('::')                     # ifInOctets.1 = Counter32: 5217689
        mib_category = file_line[1].split('=')           # Counter32: 5217689
        mib_value= mib_category[1].split(':')            # 5217689\n
        value = mib_value[-1].strip()                    # 5217689
        mib_name = mib_category[0].split('.')
        if mib_name[0] in list_of_value_mib():
            mib = mib_name[0] + mib_name[1]
            while True:
                try:
                    db.execute('create table {} (date text, datetime text, value text)'.format(mib))
                    print('Creating table ' + mib)
                except sqlite3.OperationalError:
                    break
            db.execute('insert into {} (date, datetime, value) values (?, ?, ?)'.format(mib), (strftime("%Y%m%d",), strftime("%H:%M:%S", ), value))
            db.commit()


for i in range(0, 100):
    insert_data()
    cursor = db.execute('select * from ifInOctets1')
    print(cursor.fetchall())
    sleep(5)