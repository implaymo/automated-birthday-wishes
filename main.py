##################### Extra Hard Starting Project ######################
import os

import pandas as pd
import datetime as dt
import smtplib
import random


# Gets today's date
datetime = dt.datetime.now()
date = datetime.date()
day = date.day
month = date.month
year = date.year

my_email = "pythonuser112@gmail.com"
password = "vuvemheklbeqqahu"

info = {'name': ['Cristina', 'Joca', 'Marta'],
        'email': ['pythonuser112@gmail.com', 'pythonuser112@gmail.com', 'pythonuser112@gmail.com'],
        'year': [2023, 2023, 2023],
        'month': [10, 10, 10],
        'day': [31, 31, 31]}

# Stores info as a dataframe and writes it to a CSV file
df = pd.DataFrame(info)
df.to_csv("birthdays.csv", index=False)

# Reads birthday's file
read_birthday_file = pd.read_csv("birthdays.csv")
info_dict = read_birthday_file.to_dict("records")


# Checks if today's date is the same as user birthday date
for dictionary in info_dict:
    if dictionary["month"] == month and dictionary["day"] == day:
        folder_path = "letter_templates"
        # Gets every file that ends with txt at folder_path
        file_list = [folder for folder in os.listdir(folder_path) if folder.endswith(".txt")]
        random_letter = random.choice(file_list)
        random_letter_path = os.path.join(folder_path, random_letter)
        # Opens a random letter and switches [NAME] with person's name
        with open(random_letter_path, "r") as letter_file:
            letter_content = letter_file.read()
        new_name = dictionary["name"]
        new_content = letter_content.replace("[NAME]", new_name)
        # Sends letter to person's email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=dictionary["email"],
                                msg=f"Subject: Birthday wishes\n\n {new_content}")





