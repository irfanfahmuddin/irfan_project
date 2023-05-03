import mysql.connector
import pandas as pd
import numpy as np
import os
import datetime as dt
import dateutil.relativedelta
import calendar
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime, date

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = 'irfan.fahmuddin@byru.id'
toaddr = ['irfanfahm96@gmail.com']

bccaddr = 'irfan.fahmuddin@byru.id'
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)

msg['Bcc'] = bccaddr
msg['Subject'] = "Data"

body = """
test data

"""
msg.attach(MIMEText(body, 'plain'))

filename = "Kasbon %s.csv"% today
# filename = "test %s.xlsx"% today

# attachment = open("C:\\Users\\Desktop\\file.xlsx", 
# "rb")

attachment = open("Data_Kasbon %s.csv"% today, "rb")
# attachment = open("../Data/test %s.xlsx"% today, "rb")
# attachment = kasbon_sallary

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "fkrehobgyvrezpck") #onetime password irfan

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


