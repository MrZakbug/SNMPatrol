import sqlite3
import random
from time import strftime, sleep

files = ['MIB16', 'MIB2', 'MIB3', 'MIB4', 
        'MIB5', 'MIB6', 'MIB7', 'MIB8', 'MIB9',
        'MIB10', 'MIB11', 'MIB12', 'MIB13', 'MIB14',
        'MIB15', 'MIB16', 'MIB17', 'MIB18', 'MIB19', 'MIB20', ]


#Read file and create a list of MIBs of value
def listOfValueMib():
    #Read file with MIBs we want
    valueMibsPath = 'required\\neededMIB.txt'
    readFile = open(valueMibsPath,'r')
    #Create a list
    valueMibs = []
    for line in readFile:
        valueMibs.append(line.rstrip('\n'))
    readFile.close()
    return valueMibs

#Create a database
db = sqlite3.connect('SNMPatrol.db')

def insertData():
#load and insert data
    mibTrap = 'required\\' + random.choice(files) + '.txt'
    readFile = open(mibTrap, 'r')
    for line in readFile:                               #IF-MIB::ifInOctets.1 = Counter32: 5217689
        fileLine = line.split('::')                     #ifInOctets.1 = Counter32: 5217689
        mibCategory = fileLine[1].split('=')            #Counter32: 5217689
        mibValue= mibCategory[1].split(':')             #5217689\n
        value = mibValue[-1].strip()                    #5217689
        mibName = mibCategory[0].split('.')
        if mibName[0] in listOfValueMib():
            mib = mibName[0] + mibName[1]
            while True:
                try:
                    db.execute('create table {} (date text, datetime text, value text)'.format(mib))
                    print('Creating table ' + mib)
                except sqlite3.OperationalError:
                    break
            db.execute('insert into {} (date, datetime, value) values (?, ?, ?)'.format(mib), (strftime("%Y%m%d",), strftime("%H:%M:%S", ), value))
            db.commit()


for i in range(0, 100):
    insertData()
    cursor = db.execute('select * from ifInOctets1')
    print(cursor.fetchall())
    sleep(5)