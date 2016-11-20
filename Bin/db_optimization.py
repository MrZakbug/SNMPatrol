import sqlite3
import datetime
from process_data import import_data, avg_value, delete_data


db = sqlite3.connect('SNMPatrol.db')


def last_week_optimization(table_name, start_date, end_date, start_time, end_time):
    today = datetime.date.today()
    for day in range(8, 15):
        for hour in range(0, 24):
            if len(hour) < 2:
                hour = '0' + str(hour)
            else:
                hour = str(hour)
            avg = avg_value(import_data(table_name, today + datetime.timedelta(days=day),
                                        today + datetime.timedelta(days=day), hour + ':00:00',
                                        str(int(hour)+1)) + ':00:00')
            delete_data(import_data(table_name, today + datetime.timedelta(days=day),
                                    today + datetime.timedelta(days=day), hour + ':00:00', str(int(hour)+1) + ':00:00'))
            db.execute('INSERT INTO {} (DATE, DATETIME, VALUES) VALUES(?, ?, ? )'.format(table_name),
                       (today + datetime.timedelta(days=day), hour + ':30:00', avg))
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
    # last_week_optimization('ifInOctets1', '2016/11/12', '2016/11/12', '00-00-01', '23-01-05')
    print(datetime.date.today())