import email, smtplib, ssl
import pandas as pd

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receivers = pd.read_excel('receivers.xlsx', usecols="A, C")

subject = "Webinar Nasional & Talkshow Invasi Udayana 2022"
sender_email = "mahardikagede0@gmail.com"
password = "aezoyxkcfzqpagne"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for i in receivers.index:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject
        
        body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <p>
                Selamat pagi.
            </p>
            <p>
                Terima kasih sudah mendaftar webinar kami. Nomor tiket anda <b>{receivers['nomor'][i]}</b>.<br>
                Silakan bergabung grup berikut <a href="https://t.me/+gAc1mWuhdDc2ZDFl">https://t.me/+gAc1mWuhdDc2ZDFl</a> dengan format <b>NO TIKET_NAMA</b> untuk informasi lebih lanjut. 
            </p>
            <p>
                Jika terdapat kendala dapat menghubungi contact person di bawah ini:<br>
                <a href="http://invasiudayana.com/CpWebnasDanTalkshowInvasi">http://invasiudayana.com/CpWebnasDanTalkshowInvasi</a>
            </p>
        </body>
        </html>
        """
        message.attach(MIMEText(body, "html"))

        file_send = f"{receivers['nomor'][i]}.png"
        with open(file_send, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_send}"
        )

        message.attach(part)
        text = message.as_string()

        server.sendmail(sender_email, receivers['email'][i], text)
        print(f"{receivers['email'][i]} send successfully")