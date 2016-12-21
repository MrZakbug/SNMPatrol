import import_data


class Device:
    def __init__(self, name, ip, dns, os, d_type):
        self.name = name
        self.address_Ip = ip
        self.dns_name = dns
        self.os = os
        self.d_type = d_type
        self.list_of_mibs = import_data.list_of_value_mib(self.name)

    def ping(self):
        """
        Returns True if host responds to a ping request
        """
        import os
        import platform

        # Ping parameters as function of OS
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

        # Ping
        return os.system("ping " + ping_str + " " + self.address_Ip) == 0


if __name__ == '__main__':
    dictionary = {'Device Name': 'SERV-01',
                  'Device IP Address': '8.8.8.8',
                  'Device DNS': 'SERV-01',
                  'Device OS': 'Windows',
                  'Device Type': 'Server'}

    device1 = Device(dictionary['Device Name'],
                     dictionary['Device IP Address'],
                     dictionary['Device DNS'],
                     dictionary['Device OS'],
                     dictionary['Device Type'])

    print(device1.ping())
    print(device1.list_of_mibs)