import sqlite3

#Connect to DB
db = sqlite3.connect('SNMPatrol.db')

#Fetch data from the table and put into list variable
def importTimedData(tableName,startDate, endDate, startTime, endTime):
	values = []
	for value in db.execute('select value from {} where (date between {} and {}) and (datetime between {} and {})'\
		.format(tableName, startDate, endDate, startTime, endTime)):
		values.append(value[0])
	return values

def importDatedData(tableName,startDate, endDate):
	values = []
	for value in db.execute('select value from {} where date between {} and {}'\
		.format(tableName, startDate, endDate)):
		values.append(value[0])
	return values

def importData(tableName):
	values = []
	for value in db.execute('select value from {}'.format(tableName)):
		values.append(value[0])
	return values
	
#Count the avg and return
def avgValue(values):
	value = 0
	count =0
	for v in values:
		value += int(v)
		count += 1
	avg = int(value/count)
	return avg

def maxValue(values):
	return max(values)

def minValue(values):
	return min(values)


print(avgValue(importData('ifInOctets1')))
print(maxValue(importData('ifInOctets1')))
print(minValue(importData('ifInOctets1')))

#print(importDatedData('ifInOctets1', '20141013', '20161015'))

#cursor = db.execute('select * from ifInOctets1')
#print(cursor.fetchall())
#
#
#print(importTimedData('ifInOctets1','20141013', '20161014', '10:14:34', '16:18:40'))
