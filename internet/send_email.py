# How to send emails
import datetime
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(text="", title="", from_sender=None, to_receiver=None, attachmnt=None):
    import smtplib
    import email.mime.text
    import email.mime.application
    msg = MIMEMultipart()
    msg['Subject'] = "{}".format(title)
    msg['From'] = from_sender
    msg['To'] = ', '.join(to_receiver)
    body = ''
    body += '{}'.format(text)
    body += '<br><br>'
    body += 'Message sent automatically by robots at {}<br>'.format(
        datetime.datetime.now().strftime("%H:%M %d.%m.%Y"))

    # msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(body, 'html'))

    if attachmnt is not None:
        for f in attachmnt:
            fname = os.path.basename(f)
            with open(f, 'rb') as fil:
                part = email.mime.application.MIMEApplication(
                    fil.read(),
                    Name=fname
                )
                part['Content-Disposition'] = 'attachment; filename=\"{}\"'.format(fname)
                msg.attach(part)

    server = smtplib.SMTP("milrelay.sandisk.com")
    server.sendmail(sender, to_receiver, msg.as_string())
    server.close()


if __name__ == '__main__':
    sender = 'Queen Elizabeth <Queen_Elizabeth@wdc.com>'
    send_to = ['Guy.Barash@wdc.com']
    text = 'Always remember:\t{link}'.format(link=r'https://www.youtube.com/watch?v=EloDnA1_XEU')
    title = 'This is an example of an Email'
    attachment = None  # [r"C:\work\plygrnd\data.csv"]

    send_email(text=text,
               title=title,
               from_sender=sender,
               to_receiver=send_to,
               attachmnt=attachment)

    print("CODE COMPLETED.")
