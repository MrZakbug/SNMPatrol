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

def snmp_walk(mib,hostname = '0.0.0.0', community = 'public', version = '1')
    from easysnmp import snmp_get

    snmp_get({}, hostname={}, community={}, version={}.format(mib, hostname, community, version))


if __name__ == '__main__':
    print(ping('10.5.30.44'))