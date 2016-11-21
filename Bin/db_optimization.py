import datetime
from process_data import *


db = sqlite3.connect('SNMPatrol.db')


def last_week_optimization(table_name):
    today = datetime.date.today()
    for day in range(7, 8):
        for hour in range(0, 24):
            if hour < 10:
                current_hour = '0' + str(hour) + ':00:00'
                next_hour = '0' + str(hour) + ':59:59'
            else:
                current_hour = str(hour) + ':00:00'
                next_hour = str(hour) + ':59:59'

            day_to_optimize = today - datetime.timedelta(days=day)
            avg = avg_value(import_data(table_name, day_to_optimize, day_to_optimize, current_hour, next_hour))
            delete_data(table_name, day_to_optimize, day_to_optimize, current_hour, next_hour)
            db.execute('INSERT INTO {} (DATE, DATETIME, VALUE) VALUES(?, ?, ? )'.format(table_name),
                       (day_to_optimize, current_hour, avg))
            db.commit()


def last_month_optimization():
    pass
    # for each day
        # for each 3 hours
            # avg the values
            # delete all the values in this time stamp
            # insert avg value with specific time


def previous_months_optimization():
    pass
    # for each day
        # avg the values
        # delete all the values in this time stamp
        # insert avg value with specific time

if __name__ == '__main__':
    db = sqlite3.connect('SNMPatrol.db')
    last_week_optimization('hrDeviceDescr196608')