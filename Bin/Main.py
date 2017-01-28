import device_class
import db_optimization
import json
import multiprocessing
import os
from time import sleep, strftime


def create_device_instances():
    """
    Creates a list of device instances stated in config.json file
    """
    data_file = open(os.path.join('required', 'Config.json'), 'r')
    config = json.load(data_file)
    data_file.close()
    devices_list = []
    for device_config in config["Devices"]:
        devices_list.append(device_class.Device(device_config["Device Name"], device_config["Device IP Address"],
                                                device_config["Device DNS"], device_config["Device OS"],
                                                device_config["Device Type"], device_config["Notifications Enabled"]))
    return devices_list


def db_optimization(device_instance):
    """
    Optimizes each table of each device
    """
    for table in device_instance.device.tables:
        db_optimization.data_base_optimization(table)


def main(device_instance):
    """
    Performs SNMP walk for each device and each device's OID stated in neededOIDs-????.txt file, checks for
    warnings/errors and sends alerts mail and/or imputs the data inot the DB
    """
    print(device_instance.name)
    device_instance.snmp_walk()

if __name__ == '__main__':
    devices = create_device_instances()

    today = strftime("%Y-%m-%d", )
    optimized_today = False
    while True:
        """
        For every device in devices list starts a process of main function. If time is between 00:00;00 and 01:00:00 and
        DB was not optimized this day starts processes of optimization for each device.
        """
        for device in devices:
            process = multiprocessing.Process(target=main, args=(device,))
            process.start()

        sleep(300)

        if '00' < strftime("%H", ) < '01' and not optimized_today:
            for device in devices:
                optimization = multiprocessing.Process(target=db_optimization, args=(device,))
                optimization.start()
            optimized_today = True

        if strftime("%Y-%m-%d", ) > today:
            # Changes the status of optimization when day change and today to today's date for further checks
            today = strftime("%Y-%m-%d", )
            optimized_today = False
