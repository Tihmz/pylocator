import feedparser
import time
from datetime import datetime
import smtplib
import json
import os

email = ""
password = ""
targets = []

if not os.path.exists(".creds.txt"):
    print("Credential file not found, exiting")
    exit(1)

if not os.path.exists("config.json"):
    print("Config file not found, exiting...")
    exit(1)

with open(".creds.txt","r") as file:
    line = file.read()
    line = line.split(':')
    email = line[0]
    password = line[1].removesuffix('\n')

with open("config.json","r") as file:
    json_data = json.load(file)
    for target in json_data["subscribers"]:
        targets.append(target)

creds = (email,password)

prev_id = ""
with open("prev_id.txt",'r') as file:
    prev_id = file.read()

print("last saved ID :",prev_id)

def create_link(link):
    i1 = link.index("vendor=")
    i2 = link.index("&")
    vendor = link[i1:i2]

    result =  "https://rpilocator.com/?instock&" + vendor
    return result

def create_message(target,product):

    link = create_link(product["link"])

    message = """From: RPI Locator trought melchior <python.testhere@gmail.com>
To: To {} <{}>
Subject: {}

Hello {},

{}

Here is a link to all the raspberry pi currently available in this store:

{}

Here is a link to all the raspberry pi currently available everywhere :

https://rpilocator.com/?instock

Have a nice day !

Powered by https://rpilocator.com/
""".format(target["name"],target["email"],product["title"],target["name"],product["summary"],link)
    return message

def send_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(creds[0],creds[1])
    s.sendmail(creds[0], target["email"], message)
    s.quit()

while True:
    try:
        NewsFeed = feedparser.parse("https://rpilocator.com/feed/")
        entries = NewsFeed["entries"]
        try:
            ID = entries[0]["id"]
            if ID != prev_id:
                prev_id = ID
                with open("prev_id.txt","w") as file:
                    file.write(ID)
                print(datetime.now(),ID,entries[0]["title"])
                for target in targets:
                    message = create_message(target,entries[0])
                    send_mail(message)
            else:
                time.sleep(9)
        except IndexError:
            pass
    except ConnectionResetError:
        pass
