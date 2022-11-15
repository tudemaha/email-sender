import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Webinar Nasional & Talkshow Invasi Udayana 2022"
sender_email = ""
password = ""

body = """
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
        Terima kasih sudah mendaftar webinar kami. Nomor tiket anda <b>S0158</b>.<br>
        Silakan bergabung grup berikut <a href="https://t.me/+gAc1mWuhdDc2ZDFl">https://t.me/+gAc1mWuhdDc2ZDFl</a> dengan format <b>NO TIKET_NAMA</b> untuk informasi lebih lanjut. 
    </p>
    <p>
        Jika terdapat kendala dapat menghubungi contact person di bawah ini:<br>
        <a href="http://invasiudayana.com/CpWebnasDanTalkshowInvasi">http://invasiudayana.com/CpWebnasDanTalkshowInvasi</a>
    </p>
</body>
</html>
"""

message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject

message.attach(MIMEText(body, "html"))

receiver_email = ["agungmahadana07@gmail.com", "gusnanda1170@gmail.com", "agusdharma48@gmail.com", "nandaptr.official@gmail.com", "arywidhiana170503@gmail.com", "gede.mahardika@yahoo.co.id"]
file_send = "test.png"

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

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for email in receiver_email:
        server.sendmail(sender_email, email, text)
        print(f"{email} send successfully")