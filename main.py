import random
import smtplib
import os

MY_EMAIL = os.environ.get("ty_python_gmail_em")
MY_PASSWORD = os.environ.get("ty_python_gmail_pas")

TO_EMAIL = os.environ.get("tr_bd_yr_gm_em")



with open(file="quotes.txt", mode="r") as quote_file:
    contents = quote_file.readlines()
    quote = random.choice(contents)
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:Quote to start the week!\n\n{quote}")
