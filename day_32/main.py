# import smtplib

# my_email = "<type your email>"
# password = "<custom app password>"

# with smtplib.SMTP("smtp.<your mail smtp>.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     message = "Subject: <subject>\n\n<Body of the email.>"
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="<email to send>", 
#         msg=message
#     )
    
import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 5:
    
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        
    print(random.choice(quotes))