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
    alert_type = {'ifInOctets1': 'latency'}

    msg = "Hello!\n\nThis is an alert from your SNMPatrol system.\
    \n\nThis mail's purpose is to report that your hardware named {} have just encountered a problem\
    with {}. The last value reported is {} which is {} percent higher than medium value ({}).\
    \n\nSincerely,\nYour SNMPatrol.".format(hardware_name, alert_type[mib], trigger,
                                            round(((int(trigger)/int(medium) - int('1')) * 100), 2), medium)
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

    # send_email(sender, recipients, email_subject, create_msg(hardware_name, mib, trigger, overMedium))
    # send_email(email_login, recipients, email_subject, create_msg('PL-S001', '1', '98', '56'))
    print(get_email_addresses())