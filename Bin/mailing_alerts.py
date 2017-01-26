import smtplib
import json

email_login = ''
email_password = ''

email_subject = 'Subject: SNMPatrol Alert'


def create_msg(hardware_name, mib, trigger, medium):
    """
    Checks what type of alert is assigned to mib provided
    and return proper message based on values provided ready to sent
    """
    alert_type = {'ifInOctets': 'number of data coming to interface port',
                  'ifInOctets.1': 'number of data coming to interface 1 port',
                  'ifInOctets.2': 'number of data coming to interface 2 port',
                  'ifInOctets.3': 'number of data coming to interface 3 port',
                  'ifInOctets.4': 'number of data coming to interface 4 port',
                  'ifOutOctets': 'number of data coming from interface port',
                  'ifOutOctets.1': 'number of data coming from interface 1 port',
                  'ifOutOctets.2': 'number of data coming from interface 2 port',
                  'ifOutOctets.3': 'number of data coming from interface 3 port',
                  'ifOutOctets.4': 'number of data coming from interface 4 port',
                  'ifMtu.1': 'checking MTU of port 1', 'ifMtu.2': 'checking MTU of port 2',
                  'ifSpeed.21': 'checking speed of port 1', 'ifSpeed.2': 'checking speed of port 2',
                  'ifAdminStatus.2': 'Status of port 2', 'ifOperStatus.2': 'Status of port 2',
                  'laLoad.1': 'system load from last 1 min', 'laLoad.2': 'system load from last 5 min',
                  'laLoad.3': 'system load from last 15 min', 'ssCpuUser.0': 'percentage usage of CPU by users',
                  'ssCpuRawUser.0': 'usage of CPU by users', 'ssCpuSystem.0': 'percentage usage of CPU by system',
                  'ssCpuRawSystem.0': 'usage of CPU by system', 'ssCpuIdle.0': 'percentage time of CPU being idle',
                  'ssCpuRawIdle.0': 'time of CPU being idle', 'hrProcessorLoad.196608': 'CPU 1 Load',
                  'hrProcessorLoad.196609': 'CPU 2 Load', 'memTotalSwap.0': 'avaiable swap space',
                  'memAvailSwap.0': 'used swap space', 'memTotalReal.0': 'avaiable RAM space',
                  'memAvailReal.0': 'used RAM space', 'memTotalFree.0': 'free RAM space',
                  'memShared.0': 'shared RAM space', 'memBuffer.0': 'buffered RAM space',
                  'memCached.0': 'cached RAM space', 'dskAvail.1': 'avaiable disc 1 space',
                  'dskUsed.1': 'used disc 1 space', 'hrStorageSize.1': 'size of storage 1',
                  'hrStorageUsed.1': 'usage of storage 1', 'dskPercent.1': 'percentage usage of storage 1',
                  'dskPercentNode.1': 'percentage usage of inods of storage 1', 'sysUpTimeInstance': 'uptime'
                  }

    msg = "Hello!\n\nThis is an alert from your SNMPatrol system.\
    \n\nThis mail's purpose is to report that your hardware named {} have just encountered a problem\
    with {}. The last value reported is {} which is {} percent higher than medium value ({}).\
    \n\nSincerely,\nYour SNMPatrol.".format(hardware_name, alert_type[mib], trigger,
                                            round(((int(trigger)/int(medium) - int('1')) * 100), 2), medium)
    return msg


def no_response_alert(hardware_name, error_indication):
    msg = "Hello!\n\nThis is a critical alert from your SNMPatrol system. \n\nThis mail's purpose is to report that" \
          " your hardware named {} encountered a critical error.\n\nThe error indication/status received is:\n " \
          "'".format(hardware_name) + error_indication + "'\n\nPlease check you device\n\nSincerely,\nYour SNMPatrol."
    return msg


def get_email_addresses():
    recipients = []
    data_file = open('required\\Config.json', 'r')
    config = json.load(data_file)
    data_file.close()
    for user in config["Users"]:
        recipients.append(user['User Email'])
    return recipients


def send_email(sender, subject, message):
    recipients = get_email_addresses()
    try:
        conn = smtplib.SMTP('smtp.gmail.com')  # create connection

        conn.ehlo()  # Identify yourself to an ESMTP server
        conn.starttls()  # Put the SMTP connection in TLS
        conn.login(email_login, email_password) # Log in
        conn.sendmail(sender, recipients, '{}\n\n{}'.format(subject, message))
        conn.quit()
    except TypeError as e:
        print(e)
        pass


if __name__ == '__main__':
    # print(create_msg('Server01', 'ifOutOctets.3', 89, 65))
    # send_email(sender, recipients, email_subject, create_msg(hardware_name, mib, trigger, overMedium))
    # send_email(email_login, recipients, email_subject, create_msg('PL-S001', '1', '98', '56'))
    # print(get_email_addresses())
    print(no_response_alert('dupa', 'dupa'))