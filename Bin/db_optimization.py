import sqlite3
from process_data import *

def connect_to_db():
    db = sqlite3.connect('SNMPatrol.db')


def last_week_optimization(table_name, start_date, end_date, start_time, end_time):
    connect_to_db()
    for day in range(0, 7):
        for hour in range(0, 24):
            process_data.import_data(table_name, start_date, end_date, start_time, end_time)
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