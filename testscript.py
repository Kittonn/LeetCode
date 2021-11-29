import datetime
today = datetime.date.today()
someday = datetime.date(2022, 3, 12)
diff = someday - today
print(diff.days)