import import_data
import mailing_alerts as mail
from pysnmp.hlapi import *


class Device:
    def __init__(self, name, ip, dns, os, d_type):
        self.name = name
        self.address_Ip = ip
        self.dns_name = dns
        self.os = os
        self.d_type = d_type
        self.list_of_oids = import_data.list_of_value_mib(self.name)
        self.tables = []

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

    def snmp_walk(self):

        for oid in self.list_of_oids:
            error_indication, error_status, error_index, var_binds = next(
                getCmd(SnmpEngine(),
                       CommunityData('public'),
                       UdpTransportTarget((self.address_Ip, 161)),
                       ContextData(),
                       ObjectType(ObjectIdentity(oid)))
            )

            if error_indication:
                mail.send_email(mail.email_subject, mail.no_response_alert(self.name, error_indication))
                break
            elif error_status:
                error = '{} at %{}'.format(error_status.prettyPrint(),
                                           error_index and var_binds[int(error_index) - 1][0] or '?')
                mail.send_email(mail.email_subject, mail.no_response_alert(self.name, error))
                break
            else:
                for varBind in var_binds:
                    m = varBind[0].prettyPrint()
                    table_name = '_'.join([self.name, m.split('::')[1]]).join(['"', '"'])
                    if table_name not in self.tables:
                        self.tables.append(table_name)
                    mib = m.split('::')[1]
                    import_data.insert_data(table_name, mib, str(varBind[1]), self.name)

if __name__ == '__main__':
    dictionary = {'Device Name': 'test',
                  'Device IP Address': '8.8.8.8',
                  'Device DNS': 'test',
                  'Device OS': 'Windows',
                  'Device Type': 'Server'}

    device1 = Device(dictionary['Device Name'],
                     dictionary['Device IP Address'],
                     dictionary['Device DNS'],
                     dictionary['Device OS'],
                     dictionary['Device Type'])

    #print(device1.ping())
    #print(device1.list_of_oids)
    device1.snmp_walk()