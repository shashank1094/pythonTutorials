# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
# Python code to illustrate Sending mail from
# your Gmail account

# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
# https://myaccount.google.com/security  #Generate a App password for your account


def send_email_without_attachment(from_email, password, recipients, subject, body):
    import smtplib

    recipients = recipients if isinstance(recipients, list) else [recipients]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (from_email, ", ".join(recipients), subject, body)
    try:
        # creates SMTP session
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()

        # Authentication
        server.login(from_email, password)

        # sending the mail
        server.sendmail(from_email, recipients, message)
        server.close()
        print("Successfully sent the mail to {}.".format(",".join(recipients)))
    except:
        print("Failed to send mailto {}.".format(",".join(recipients)))


def send_email_with_attachment(from_email, password, recipients, subject, body, file_name, file_path):
    # libraries to be imported
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    recipients = recipients if isinstance(recipients, list) else [recipients]

    for recipient in recipients:
        try:
            # instance of MIMEMultipart
            msg = MIMEMultipart()
            # storing the senders email address
            msg['From'] = from_email
            # storing the receivers email address
            msg['To'] = recipient
            # storing the subject
            msg['Subject'] = subject
            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))
            # open the file to be sent
            filename = file_name
            attachment = open(file_path, "rb")
            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')
            # To change the payload into encoded form
            p.set_payload((attachment).read())
            # encode into base64
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            # attach the instance 'p' to instance 'msg'
            msg.attach(p)
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            # Authentication
            s.login(from_email, password)
            # Converts the Multipart msg into a string
            text = msg.as_string()
            # sending the mail
            s.sendmail(from_email, recipient, text)
            # terminating the session
            s.quit()
            print('Successfully sent the mail to {}.'.format(recipient))
        except:
            print("Failed to send mailto {}.".format(recipient))


if __name__ == "__main__":
    # send_email_without_attachment("sender_email_id@gmail.com",
    #                               "app_generated_password",
    #                               ["receiver1_email_id@gmail.com","receiver2_email_id@gmail.com"],
    #                               "Testing email",
    #                               "I sent this using python.")
    # send_email_with_attachment("sender_email_id@gmail.com",
    #                            "app_generated_password",
    #                            ["receiver1_email_id@gmail.com", "receiver2_email_id@gmail.com"],
    #                            "Email's subject",
    #                            "Sent using python.",
    #                            "kuch_bhi_name.py",
    #                            "/path/to/file/abc.py")
    print("Hello World!")
