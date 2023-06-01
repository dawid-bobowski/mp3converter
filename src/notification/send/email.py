import smtplib, os, json, ssl
from email.mime.text import MIMEText

def notification(message):
    # try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        receiver_address = message["username"]

        msg = MIMEText(f"mp3 file_id: {mp3_fid} is now ready!")
        msg["Subject"] = "Download your MP3"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        context = ssl.create_default_context()

        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls(context=context)
        session.login(sender_address, sender_password)
        session.sendmail(sender_address, receiver_address, msg.as_string())
        session.quit()
        print("Mail sent")
    # except Exception as err:
    #     print(err)
    #     return err