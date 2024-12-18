from flask import Flask, render_template
import smtplib
from email.mime.text import MIMEText
import pyrebase
import time


app = Flask(__name__)

@app.route('/')
def hello_world():
  
    config = {
      "apiKey": "AIzaSyB1w5Z-mhdwgK2Q_IAl5OfCmFdq9BHZH2I",
      "authDomain": "savesoil-87f59.firebaseapp.com",
      "databaseURL": "https://savesoil-87f59-default-rtdb.firebaseio.com",
      "projectId": "savesoil-87f59",
      "storageBucket": "savesoil-87f59.firebasestorage.app",
      "messagingSenderId": "599511712569",
      "appId": "1:599511712569:web:6c0b343b7d0b4309681ee8",
      "measurementId": "G-93CJXMS17G"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

    mail = db.child("JoinUsMessage").child("Email").get()
    email = mail.val()

    name = db.child("JoinUsMessage").child("Name").get()
    namebg = name.val()

    time.sleep(1)

    
    subject = "Hey" + " " + namebg + "," + " you have recieved a message from YUVA!"
    body = "Hello"+ " " + namebg + ", " + "\n \n Hope this mail finds you well! \n \n We are happy to recieve your message. We shall get back to you in a day or two (24 to 48 hours). \n \n We value your patience. If you still wish to connect to us, you can always give us a ring on +91 9482542303 or a leave a WhatsApp message on the same. \n \n Waiting to eagerly connect to you. \n \n Thank you \n \n Reagrds \n \n Akhil K \n Founder \n YUVA "

    sender = "iamyuva.org@gmail.com"
    recipients = [email]
    password = "svkk nskz tvxt wnib"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
  
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
