import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sumanthhere1234@gmail.com','qczr ugrn gvzl opje')
    msg=EmailMessage()
    msg['From']='sumanthhere1234@gmail.com'
    msg["Subject"]=subject
    msg['To']=to 
    msg.set_content(body)
    server.send_message(msg)
    server.quit()