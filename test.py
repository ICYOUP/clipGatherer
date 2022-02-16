import datetime
now = datetime.datetime.now()
print(now)
if (((now.strftime("%w") == str(2) or now.strftime("%w") == str(3)) and now.hour == 22)):
    print("poggers")