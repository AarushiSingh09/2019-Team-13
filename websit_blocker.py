import time
from datetime import datetime as dt

host_temp="hosts"
host_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websit_list=["www.facebook.com", "facebook.com","youtube.com","www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8)<=dt.now()<=dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print("working hours!")
        with open(host_path, 'r+') as file:
            content=file.read()
            for website in websit_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " "+ website+ "\n")

    else:
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websit_list):
                    file.write(line)
            file.truncate()
        print("Read your books!.This is not a free time.")
    time.sleep(5)
