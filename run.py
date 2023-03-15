import feedparser
import time
from datetime import datetime
import smtplib
import json
import os

import utils.rpi
import utils.f0
import utils.lab401
import utils.joom
email = ""
password = ""
targets = []
savefile = ".prev_update.json"
f0_vendors = {}

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

    for vendor in json_data["flipper_url"]:
        f0_vendors[vendor] = json_data["flipper_url"][vendor]

creds = (email,password)

ids = {
    "id_rpi":"",
    "f0_instock":"no",
    "401_instock":"no",
    "joom_instock":"no"
}

if not os.path.exists(savefile):
    file = open(savefile,'x')
    file.close()

with open(savefile,'r') as file:
    json_data = json.load(file)
    for entry in json_data:
        ids[entry] = json_data[entry]


print("last saved ID :",ids["id_rpi"])

def save_ids():
    with open(savefile,"w") as file:
        json.dump(ids,file)

def send_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(creds[0],creds[1])
    s.sendmail(creds[0], target["email"], message)
    s.quit()

def check_rpi():
    NewsFeed = feedparser.parse("https://rpilocator.com/feed/")
    entries = NewsFeed["entries"]
    try:
        ID = entries[0]["id"]
        if ID != ids["id_rpi"]:
            prev_id = ID
            save_ids()
            print(datetime.now(),ID,entries[0]["title"])
            for target in targets:
                message = rpi.create_message(target,entries[0])
                send_mail(message)
        else:
            time.sleep(9)
    except IndexError:
        pass

def check_f0():
    page = f0.get_page(f0_vendors["f0"])
    instock = f0.check_in_stock(page)
    if instock:
        if ids["f0_instock"] == "no":
            ids["f0_instock"] = "yes"
            save_ids()
    else:
        if ids["f0_instock"] == "yes":
            ids["f0_instock"] = "no"
            save_ids()

def check_joom():
    page = joom.get_page(f0_vendors["joom"])
    instock = joom.check_in_stock(page)
    if instock:
        if ids["joom_instock"] == "no":
            ids["joom_instock"] = "yes"
            save_ids()
    else:
        if ids["joom_instock"] == "yes":
            ids["joom_instock"] = "no"
            save_ids()


def check_401():
    page = lab401.get_page(f0_vendors["lab401"])
    instock = lab401.check_in_stock(page)
    if instock:
        if ids["lab401_instock"] == "no":
            ids["lab401_instock"] = "yes"
            save_ids()
    else:
        if ids["lab401_instock"] == "yes":
            ids["lab401_instock"] = "no"
            save_ids()



while True:
    try:
        check_rpi()
    except ConnectionResetError:
        pass
