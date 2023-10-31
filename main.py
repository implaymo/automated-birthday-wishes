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


info = {'name': ['Cristina', 'Joca', 'Marta'],
        'email': ['pythonuser112@gmail.com', 'pythonuser112@gmail.com', 'pythonuser112@gmail.com'],
        'year': [2023, 2023, 2023],
        'month': [10, 10, 10],
        'day': [31, 31, 31]}

# Stores info as a dataframe and writes it to a CSV file
df = pd.DataFrame(info)
df.to_csv("birthdays.csv", index=False)

# 2. Check if today matches a birthday in the birthdays.csv
# Reads birthday's file
read_birthday_file = pd.read_csv("birthdays.csv")
info_dict = read_birthday_file.to_dict("records")

# Checks if today's date is the same as user birthday date
for line in info_dict:
    if line["year"] == year and line["month"] == month and line["day"] == day:
        folder_path = "letter_templates"
        # Gets every file that ends with txt at folder_path
        file_list = [folder for folder in os.listdir(folder_path) if folder.endswith(".txt")]
        if file_list:
            random_file_name = random.choice(file_list)

        #     random_file_path = os.path.join(folder_path, random_file_name)
        #     with open(random_file_path, "r") as letter_file:
        #         letter_lines = letter_file.readlines()
        #








# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




