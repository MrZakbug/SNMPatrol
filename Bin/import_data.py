import sqlite3
import random
from time import strftime, sleep
import mailing_alerts as mail
import process_data as process
from datetime import date, timedelta

"""
files = ['MIB16', 'MIB2', 'MIB3', 'MIB4', 'MIB5',
         'MIB6', 'MIB7', 'MIB8', 'MIB9', 'MIB10',
         'MIB11', 'MIB12', 'MIB13', 'MIB14', 'MIB15',
         'MIB16', 'MIB17', 'MIB18', 'MIB19', 'MIB20', ]
"""

def list_of_value_mib(name):
    # Read file and create a list of MIBs of value
    # Read file with MIBs we want
    value_mibs_path = 'required\\neededOIDs-' + name + '.txt'
    read_file = open(value_mibs_path, 'r')
    # Create a list
    value_mibs = []
    for line in read_file:
        value_mibs.append(line.rstrip('\n'))
    read_file.close()
    return value_mibs

"""
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
"""

def insert_data(table_name, value):
    # Connect/creates a database, creates tables if don't exist, puts data into
    db = sqlite3.connect('SNMPatrol.db')  # Create a database

    try:
        db.execute('create table {} (date text, datetime text, value text)'.format(table_name))
        print('Creating table ' + table_name)
    except sqlite3.OperationalError:
        print('Table {} already exists.'.format(table_name))
    db.execute('insert into {} (date, datetime, value) values (?, ?, ?)'.format(table_name),
               (strftime("%Y-%m-%d", ), strftime("%H:%M:%S", ), value))
    db.commit()
    warning_trigger(table_name, value)


def warning_trigger(m, value):
    today = date.today()
    avg = process.avg_value(process.import_data(m, today - timedelta(days=1), today))
    if type(avg) is int or type(avg) is float:
        if value > avg*5:
            mail.send_email(mail.sender, mail.recipients, mail.email_subject, mail.create_msg('PL-S001', m, value, avg))
    else:
        return avg


    '''
def insert_test_data():
    start_date = date(2016, 11, 1).toordinal()
    end_date = date.today().toordinal()

    db = sqlite3.connect('SNMPatrol.db')  # Create a database
    mib, value = get_mib_list_values()  # Assigns values from get_mib_list_values function
    for m in mib:
        while True:
            try:
                db.execute('create table {} (date text, datetime text, value text)'.format(m))
                print('Creating table ' + m)
            except sqlite3.OperationalError:
                break
        for i in range(1, 10001):
            random_hour = str(random.randrange(0, 24))
            if len(random_hour) < 2:
                random_hour = '0' + random_hour

            random_minute = str(random.randrange(0, 60))
            if len(random_minute) < 2:
                random_minute = '0' + random_minute

            random_second = str(random.randrange(0, 60))
            if len(random_second) < 2:
                random_second = '0' + random_second

            random_time = random_hour + ':' + random_minute + ':' + random_second
            db.execute('insert into {} (date, datetime, value) values (?, ?, ?)'.format(m),
                       (date.fromordinal(random.randint(start_date, end_date)), random_time, random.randrange(20, 100)))

            db.commit()
    '''

if __name__ == '__main__':
    warning_trigger(m='ifInOctets1', value=100)
    '''
    db = sqlite3.connect('SNMPatrol.db')
    for i in range(0, 100):
        insert_data()
        cursor = db.execute('select * from ifInOctets1')
        print(cursor.fetchall())
        sleep(5)
    '''