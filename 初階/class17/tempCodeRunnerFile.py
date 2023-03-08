import datetime

print(datetime.date.today())
now = datetime.date.today()
day = input("What is your birthday? ")
print(day)
birth = datetime.datetime.strptime(day, "%m/%d/%Y")
print(birth.date())
print(birth.date() - now)
