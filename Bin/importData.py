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


def get_mib_list_values():
    # Prepares a list of mibs and their values
    mib = []
    mib_trap = 'required\\' + random.choice(files) + '.txt'
    read_file = open(mib_trap, 'r')
    for line in read_file:                                          # IF-MIB::ifInOctets.1 = Counter32: 10786522
        file_line = line.split('::')                                # ['IF-MIB', 'ifInOctets.1 = Counter32: 10786522\n']
        mib_category = file_line[1].split('=')                      # ['ifInOctets.1 ', ' Counter32: 10786522\n']
        if mib_category[0].rstrip(' ') in list_of_value_mib():
            mib_value = mib_category[1].split(':')                  # [' Counter32', '10786522\n'}
            value = mib_value[-1].strip()                           # 10786522
            mib_name = mib_category[0].split('.')                   # ['ifInOctets', '1 ']
            if len(mib_name) > 1:
                mib.append(mib_name[0] + mib_name[1].rstrip(' '))
            else:
                mib.append(mib_name[0].rstrip(' '))
    return mib, value


def insert_data():
    # Connect/creates a database, creates tables if don't exist, puts data into

    db = sqlite3.connect('SNMPatrol.db')  # Create a database
    mib, value = get_mib_list_values()    # Assigns values from get_mib_list_values function
    for m in mib:
        while True:
            try:
                db.execute('create table {} (date text, datetime text, value text)'.format(m))
                print('Creating table ' + m)
            except sqlite3.OperationalError:
                print('Table {} already exists.'.format(m))
                break
        db.execute('insert into {} (date, datetime, value) values (?, ?, ?)'.format(m),
                   (strftime("%Y%m%d",), strftime("%H:%M:%S", ), value))
        db.commit()

if __name__ == '__main__':
    db = sqlite3.connect('SNMPatrol.db')
    for i in range(0, 100):
        insert_data()
        cursor = db.execute('select * from ifInOctets1')
        print(cursor.fetchall())
        sleep(5)