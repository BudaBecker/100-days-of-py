import pandas, random, smtplib
import datetime as dt

def send_happy_bd(celebrant: dict) -> None:
    rand_letter = random.randint(1,3)
    with open(f"letter_templates/letter_{rand_letter}.txt", "r") as f:
        content = f.read()
        msg = content.replace("[NAME]", celebrant["name"])
        
    my_email = "<type your email>"
    password = "<custom app password>"
    with smtplib.SMTP("smtp.<your mail smtp>.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message = f"Subject: Happy Birthday {celebrant["name"]}!\n\n{msg}"
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=celebrant["email"], 
            msg=message
        )

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient='records')

today = dt.datetime.now()
today_day = today.day
today_month = today.month

for person in data_dict:
    if (person["day"], person["month"]) == (today_day, today_month):
        send_happy_bd(person)