import sqlite3

# Connect to DB
db = sqlite3.connect('SNMPatrol.db')


def import_data(table_name, *args):
    values = []
    seq = ("'", "'")
    if len(args) == 0:
        for value in db.execute('select value from {}'.format(table_name)):
            values.append(value[0])
    if len(args) in [1, 2]:
        for value in db.execute('select value from {} where date between {} and {}'
                                    .format(table_name, args[0].join(seq), args[1].join(seq))):
            values.append(value[0])
    if len(args) in [3, 4]:
        for value in db.execute('select value from {} where (date between {} and {}) and (datetime between {} and {})'
                                    .format(table_name, args[0].join(seq), args[1].join(seq), args[2].join(seq),
                                            args[3].join(seq))):
            values.append(value[0])
    return values


def avg_value(values):
    # Count the avg and return
    value = 0
    count = 0
    avg = 0
    for v in values:
        value += int(v)
        count += 1
        avg = int(value/count)
    return avg


def max_value(values):
    return max(values)


def min_value(values):
    return min(values)


if __name__ == '__main__':

    print(avg_value(import_data('ifInOctets1', '2016/11/12', '2016/11/13')))

    print(avg_value(import_data('ifInOctets1', '2016/11/12', '2016/11/12', '00-00-01', '23-01-05')))
