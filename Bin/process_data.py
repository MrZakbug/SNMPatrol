import sqlite3

# Connect to DB
db = sqlite3.connect('SNMPatrol.db')


def import_timed_data(table_name, start_date, end_date, start_time, end_time):
    # Fetch data from the table and put into list variable
    values = []
    for value in db.execute('select value from {} where (date between {} and {}) and (datetime between {} and {})'\
                                    .format(table_name, start_date, end_date, start_time, end_time)):
        values.append(value[0])
    return values


def import_dated_data(table_name, start_date, end_date):
    values = []
    for value in db.execute('select value from {} where date between {} and {}'\
                                    .format(table_name, start_date, end_date)):
        values.append(value[0])
    return values


def import_data(table_name):
    values = []
    for value in db.execute('select value from {}'.format(table_name)):
        values.append(value[0])
    return values


def avg_value(values):
    # Count the avg and return
    value = 0
    count =0
    for v in values:
        value += int(v)
        count += 1
        avg = int(value/count)
    return avg


def max_value(values):
    return max(values)

def min_value(values):
    return min(values)


print(avg_value(import_data('ifInOctets1')))
print(max_value(import_data('ifInOctets1')))
print(min_value(import_data('ifInOctets1')))

# print(import_dated_data('ifInOctets1', '20141013', '20161015'))

# cursor = db.execute('select * from ifInOctets1')
# print(cursor.fetchall())
#
#
# print(import_timed_data('ifInOctets1','20141013', '20161014', '10:14:34', '16:18:40'))
