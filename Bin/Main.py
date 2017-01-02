from device_class import Device
import json

with open('required\\Config.json', 'r') as data_file:
    config = json.load(data_file)
print(config["Devices"])
devices = []
for device_config in config["Devices"]:
    devices.append(Device(device_config["Device Name"], device_config["Device IP Address"], device_config["Device DNS"],
                          device_config["Device OS"],device_config["Device Type"]))


devices[0].ping()