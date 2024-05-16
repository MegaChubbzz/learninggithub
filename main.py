import datetime

today = datetime.date.today()
future = today + datetime.timedelta(days=100)
print(future)