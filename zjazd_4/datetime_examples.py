import datetime

now = datetime.datetime.today()
my_birthday = datetime.datetime(1979,1,3)
delta = now - my_birthday

print(delta.days)