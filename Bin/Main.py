import device_class


with open('required\\Config.txt', 'r') as inf:
    config = eval(inf.read())

for device in config['Devices']:
    device['Device Name'] = device_class.Device(device['Device Name'], device['Device IP Address'],
                                                device['Device DNS'], device['Device OS'], device['Device Type'])

