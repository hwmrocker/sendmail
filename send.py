import smtplib
import docopt
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep


EMAIL_LIST = [

]


def load_config():
    import yaml
    with open("config.yaml") as fh:
        return yaml.load(fh.read())


def main(args):
    config = load_config()
    config.update(args)

    mailbox_password = config["password"]
    mailbox_name = config["username"]
    mail_server = config["server"]

    from_email = "olaf@gladis.org"
    to_email = "test@gladis.org"
    # server = smtplib.SMTP(mail_server)
    # server.login(mailbox_name, mailbox_password)
    msg = MIMEMultipart('related')
    msg['Subject'] = "Frohe Weihnachten"
    msg['From'] = from_email
    
    text = "Wir wünschen euch alle frohe Weihnachten!!!"
    html = """\
<html>
  <head></head>
  <body>
    <h1>Frohe Weihnachten</h1>
    <img src="cid:foo.bar.1337">
  </body>
</html>

    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    part3 = MIMEImage(img)
    part3.add_header('content-disposition', 'inline', filename="frohes-fest.jpg")
    part3.add_header('content-id', '<foo.bar.1337>')
    # msg = (
    # "To: %(to_email)s\r\n"
    # "From: %(from_email)s\r\n"
    # "Content-type: text/plain\r\n"
    # "Subject: frohe Weihnachten\r\n"
    # "\r\n"
    # "Hallo Test\r\n"
    # )
    for to_email in EMAIL_LIST:
        msg['To'] = to_email
        server.sendmail(from_email, to_email,msg.as_string())
        sleep(60)


    server.quit()
if __name__ == "__main__":
    main({})
