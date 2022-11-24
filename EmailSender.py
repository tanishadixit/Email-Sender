import smtplib #Simple Mail Transfer Protocol Library --> sending mail to any internet machine with localhost 465.
from password import Password #password must be secured in an another file to make your email account protected. Import that password's file wherever you want.

email_sender = '' #enter your email by using whom you were taken the authentication by gmail
email_password = Password

sent_from = email_sender
to = ""
subject = "Email Sender"
body = "This mail has been sent by email sender which is coded in python. And the coder is Tanisha Dixit."

# % --> concatenate the two strings
# %s --> is used where the string should be specified. 

email_text = """\
    From: %s  
    To: %s
    Subject: %s

    %s
""" % (sent_from, to, subject, body)

try: 
    #server is an object of smtplib
    #SSL --> is required from beginning of the connection 
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
    # Extended helo (ehlo)--> command is sent by an email server to identify itself 
    # when connecting to another email server to start the process of sending an email. 
    server.ehlo()
    server.login(email_sender, email_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print("Email is sent.")

except:
    print ("Something went wrong...")