import smtplib
from_name = 'Random Name'
from_addr = 'yourusername@gmail.com'
to_name = 'enter recipients name'
to_addr = 'david@someemail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
subject = 'Enter Subject Of Email'
msg = 'you actually type email here!!'

message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)

# Credentials (if needed)
username = 'yourusername@gmail.com'
password = 'yourpassword'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 