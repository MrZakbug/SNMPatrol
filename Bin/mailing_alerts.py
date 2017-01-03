import smtplib


email_login = ''
email_password = ''
recipients = ['', '']
email_subject = 'Subject: SNMPatrol Alert'


def create_msg(hardware_name, mib, trigger, medium):
    """
    Checks what type of alert is assigned to mib provided
    and return proper message based on values provided ready to sent
    """
    alert_type = {'ifInOctets1': 'latency'}

    msg = "Hello!\n\nThis is an alert from your SNMPatrol system.\
    \n\nI am writing to report that your hardware named {} have just encountered a problem\
    with {}. The last value reported is {} which is {} percent higher than medium value ({}).\
    \n\nSincerely,\nYour SNMPatrol.".format(hardware_name, alert_type[mib], trigger,
                                            round(((int(trigger)/int(medium) - int('1')) * 100), 2), medium)
    return msg


def send_email(sender, receiver, subject, message):
    try:
        conn = smtplib.SMTP('smtp.gmail.com')  # create connection

        conn.ehlo()  # Identify yourself to an ESMTP server
        conn.starttls()  # Put the SMTP connection in TLS
        conn.login(email_login, email_password) # Log in
        conn.sendmail(sender, receiver, '{}\n\n{}'.format(subject, message))
        conn.quit()
    except TypeError as e:
        print(e)
        pass


if __name__ == '__main__':

    # send_email(sender, recipients, email_subject, create_msg(hardware_name, mib, trigger, overMedium))
    send_email(email_login, recipients, email_subject, create_msg('PL-S001', '1', '98', '56'))
