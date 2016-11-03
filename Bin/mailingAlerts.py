import smtplib


email_login = ''
email_password = ''
sender = email_login
recipents = ['', '']
email_subject = 'SNMPatrol Alert'
email_message = "This is an alert from your SNMPatrol system. Please check your hardware"


def send_email(sender, receiver, subject, message):
    conn = smtplib.SMTP('smtp.gmail.com') #create connection

    conn.ehlo() # Identify yourself to an ESMTP server
    conn.starttls() # Put the SMTP connection in TLS
    conn.login(email_login, email_password) # Log in 
    conn.sendmail(sender, recipents, '{} \n\n{} \n\nSincerely,\nYour SNMPatrol'.format(subject, message))
    conn.quit()



send_email(sender, recipents, email_subject, email_message)

