import smtplib
import getpass

myemail=input("Enter your email id : ")
password=getpass.getpass()
recemail=input("Enter other email : ")

#creates SMTP session

s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for za security 

s.starttls()

#Authentication

s.login(myemail,password)

#message to be sent 

message=input("Enter the Message : ")

#sending the mail
s.sendmail(myemail,recemail,message)
#teminating the session 
s.quit()