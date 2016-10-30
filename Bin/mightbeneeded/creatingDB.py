import sqlite3

def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

def main():
	readFile = open('snmpwalk_vm_rh_MIB.txt','r')

	db = sqlite3.connect('SMNPatrol.db')
	db.execute('drop table if exists MIB')
	db.execute('create table snmpwalk_vm_rh_MIB (t1 text, t2 text)')

	for line in readFile:
		mibLine = line.split('::')
		mib = mibLine[1].split('=')
		print (mib[1])

if __name__ == "__main__": main()