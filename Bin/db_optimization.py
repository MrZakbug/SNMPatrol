import sqlite3
from time import strftime, time
from process_data import *


def connect_to_db():
    db = sqlite3.connect('SNMPatrol.db')


def last_week_optimization(table_name, start_date, end_date, start_time, end_time):
    connect_to_db()
    # today_list = strftime("%Y/%m/%d",).split('/')
    # for day in range(8, 15):
        # for hour in range(0, 24):
            # process_data.import_data(table_name, today + day, today + day, start_time, end_time)
            # delete all the values in this time stamp
            # insert avg value with specific tim


def last_month_optimization():
    connect_to_db()
    # for each day
        # for each 3 hours
            # avg the values
            # delete all the values in this time stamp
            # insert avg value with specific time


def previous_months_optimization():
    connect_to_db()
    # for each day
        # avg the values
        # delete all the values in this time stamp
        # insert avg value with specific time

if __name__ == '__main__':
    last_week_optimization('ifInOctets1', '2016/11/12', '2016/11/12', '00-00-01', '23-01-05')