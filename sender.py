import smtplib 
from email.mime.text import MIMEText
# from app import email 
import logging

# logging configuration
logging.basicConfig(filename='sender.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

def send_email(receiver):
    logging.info("[def send_email][sending email: start]")
    sender = "maria.clouddev@gmail.com"

    body_of_email = "Hello, dear fella!"

    # creating message
    logging.info("[def send_email][creating message]")
    msg = MIMEText("html") # to send variable formatted => coding it to bytes
    msg["Subject"] = "Hellooooouuuuu, fella!!!"
    msg["From"] = sender
    msg["To"] = receiver

    # sending message
    try:
        logging.info("[def send_email][sending message]")
        server = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
        server.login(user="maria.clouddev@gmail.com", password="CloudDeveloper2021")
        server.sendmail(sender, receiver, msg.as_string()) # coding to string
        server.quit()

        #https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20

        print("Email sent successfully!")
    except Exception as e:
        logging.info(f"Email not sent, error : {e}")
        print(f"Email not sent, error : {e}")
    
