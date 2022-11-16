import smtplib, ssl
import pandas as pd

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receivers = pd.read_excel('receivers.xlsx', usecols="A, B, C")

sender_email = "mahardikagede0@gmail.com"
password = "aezoyxkcfzqpagne"

subject = "Webinar Nasional & Talkshow Invasi Udayana 2022"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for i in receivers.index:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        body = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Automata Tiket Webinar</title>

            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap');

                * {
                    font-family: 'Roboto', sans-serif;
                    box-sizing: border-box;
                    padding: 0;
                    margin: 0;
                }

                .container {
                    height: 100vh;
                }

                .header .text {
                    color: white;
                    padding-left: 1.55rem;
                }

                .header,
                .footer {
                    background: #090979;
                    background: linear-gradient(90deg, #090979, #8e0609 100%, #00d4ff 0);
                    color: white;
                }

                .section {
                    background: url("https://d33wubrfki0l68.cloudfront.net/static/media/fb1f349208f1d6f59c9a196fdb5dc23cabe80b4e/bg-web.4e83223833905a64c54b.jpg");
                    text-align: justify;
                    line-height: 1.5rem;
                }

                .btn-a {
                    padding: 0.8rem 5rem;
                    background-color: #090979;
                    color: white !important;
                    border: none;
                    margin: auto !important;
                    text-decoration: none;
                    border-radius: 10px;
                    border-bottom-left-radius: 30px;
                    border-top-right-radius: 30px;
                }

                .section-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 1rem;
                }

                .section-header small {
                    color: gray;
                }

                .footer {
                    text-align: center;
                    color: white;
                    padding-top: 0.5rem;
                    padding-bottom: 0.5rem;
                }
                p{
                    color: black !important;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <div class="child">
                    <table cellspading='0' cellpading='0' border='0' class='header' width='400px'
                        style='padding: 1rem 3rem; border-top-left-radius: 10px !important; border-top-right-radius: 10px !important;'>
                        <tr>
                            <td width='90px'>
                                <img src="https://raw.githubusercontent.com/imkzuma/invasiudayana/main/src/img/invasi-low.png"
                                    width="100%" class='ps-4 m-0 p-0 my-auto'>
                            </td>
                            <td width='210px' style='padding-left: 1.5rem;'>
                                <h2>Invasi Udayana</h2>
                                <small>Webinar dan Talkshow</small>
                            </td>
                        </tr>
                    </table>
                    <table class='section' cellspading='0' cellpading='0' border='0' style='padding: 2rem 1.5rem;'
                        width='400px'>
                        <tr>
                            <td align="end">
                                <small>20 November 2022</small>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p>Yth.</p>

                            </td>
                        </tr>
                        <tr>
                            <td colspan="2">
                                <smal>Peserta Webinar dan Talkshow Invasi Udayana 2022</smal>
                                <p style='padding-top: 1rem;'>
                                    Terima kasih telah melakukan pendaftaran pada Webinar dan Talkshow Invasi Udayana 2022.
                                    Berikut adalah data Anda:
                                </p>
                                <p style="padding-top: 1rem;">
                                    Nomor tiket: """ + f""" <b>{receivers['nomor'][i]}</b>
                                </p>
                                <p>
                                    Silakan bergabung grup berikut: <br/>
                                    <a href="https://t.me/+gAc1mWuhdDc2ZDFl">Grup Webinar dan Talkshow Invasi Udayana 2022</a><br>
                                    (<a href="https://t.me/+gAc1mWuhdDc2ZDFl">https://t.me/+gAc1mWuhdDc2ZDFl</a>)
                                </p>
                                <p style="padding-top: 1rem;">
                                    dengan format: <b>NoTiket_Nama</b> <br />
                                    Contoh: <b>0012_Gung Krisna</b>
                                </p>
                                <div style="padding-top: 2rem; text-align: center; width: 100%">
                                    <small style = 'color: black !important;'>
                                        <b>
                                            Terdapat kendala? Silakan hubungi contact person berikut.
                                        </b>
                                    </small>

                                </div>
                                <div style='text-align: center; margin-top: 1rem;'>
                                    <a href='https://invasiudayana.com/CpWebnasDanTalkshowInvasi' class='btn-a'>
                                        Contact Person
                                    </a>
                                </div>
                            </td>
                        </tr>
                    </table>
                    <table cellspading='0' class = 'footer' cellpading='0' border='0' width='400px' style = 'border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;'>
                        <tr>
                            <td align="center" width = '400px'>
                                <small>&copy; Invasi Udayana 2022</small>
                            </td>
                        </tr>
                    </table>

                </div>
            </div>

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