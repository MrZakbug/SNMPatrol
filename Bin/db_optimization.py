import datetime
from process_data import *


db = sqlite3.connect('SNMPatrol.db')


def last_week_optimization(table_name):
    today = datetime.date.today()
    for day in range(7, 15):
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


def last_month_optimization(table_name):
    today = datetime.date.today()
    for day in range(15, 31):
        for hour in range(0, 24, 3):
            if hour < 7:
                current_hour = '0' + str(hour) + ':00:00'
                next_hour = '0' + str(hour + 2) + ':59:59'
            elif hour == 9:
                current_hour = '0' + str(hour) + ':00:00'
                next_hour = str(hour + 2) + ':59:59'
            else:
                current_hour = str(hour) + ':00:00'
                next_hour = str(hour + 2) + ':59:59'

            day_to_optimize = today - datetime.timedelta(days=day)
            avg = avg_value(import_data(table_name, day_to_optimize, day_to_optimize, current_hour, next_hour))
            delete_data(table_name, day_to_optimize, day_to_optimize, current_hour, next_hour)
            db.execute('INSERT INTO {} (DATE, DATETIME, VALUE) VALUES(?, ?, ? )'.format(table_name),
                       (day_to_optimize, current_hour, avg))
            db.commit()


def previous_months_optimization(table_name):
    today = datetime.date.today()
    for day in range(31, 91):
        day_to_optimize = today - datetime.timedelta(days=day)
        avg = avg_value(import_data(table_name, day_to_optimize, day_to_optimize))
        delete_data(table_name, day_to_optimize, day_to_optimize)
        db.execute('INSERT INTO {} (DATE, DATETIME, VALUE) VALUES(?, ?, ? )'.format(table_name),
                   (day_to_optimize, '12:00:00', avg))
        db.commit()


def data_base_optimization(table_name):
    last_week_optimization(table_name)
    last_month_optimization(table_name)
    last_month_optimization(table_name)

if __name__ == '__main__':
    db = sqlite3.connect('SNMPatrol.db')
    # previous_months_optimization('hrDeviceDescr196608')
    # last_month_optimization('hrDeviceDescr196608')
    last_week_optimization('hrDeviceDescr196608')