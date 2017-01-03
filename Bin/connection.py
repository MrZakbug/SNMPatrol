from pysnmp.hlapi import *

def snmp_walk():

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public'),
               UdpTransportTarget(('demo.snmplabs.com', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
               ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0')))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        print('here')
    else:
        for varBind in varBinds:
            print(varBind[1])
            print(' = '.join([x.prettyPrint() for x in varBind]) + '\n')

if __name__ == '__main__':
    #print(snmp_walk())
    name = 'SERV-01'
    mib = 'ifDesc.1'
    table_name = '_'.join([name, mib])
    print(table_name)
