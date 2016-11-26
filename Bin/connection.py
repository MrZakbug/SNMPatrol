from pysnmp.hlapi import *


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os
    import platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0


def snmp_walk():

    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('demo.snmplabs.com', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
    )

    if error_indication:
        print(error_indication)
    elif error_status:
        print('%s at %s' % (error_status.prettyPrint(),
                            error_index and var_binds[int(error_index) - 1][0] or '?'))
    else:
        for varBind in var_binds:
            print(' = '.join([x.prettyPrint() for x in varBind]))


if __name__ == '__main__':
    print(ping('8.8.8.8'))
    print(snmp_walk())
