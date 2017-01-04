import device_class
import json
import multiprocessing


def create_device_instances():
    data_file = open('required\\Config.json', 'r')
    config = json.load(data_file)
    data_file.close()
    devices = []
    for device_config in config["Devices"]:
        devices.append(device_class.Device(device_config["Device Name"], device_config["Device IP Address"],
                                           device_config["Device DNS"], device_config["Device OS"],
                                           device_config["Device Type"]))
    return devices


def main(device):
    print(device.name)
    device.snmp_walk()
    print(range(1, 50))

if __name__ == '__main__':
    for device in create_device_instances():
        p = multiprocessing.Process(target=main(device))
        p.start()

