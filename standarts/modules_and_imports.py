import datetime

date = input().split()
datey = int(date[0])
datem = int(date[1])
dated = int(date[2])
days = int(input())

delta = datetime.timedelta(days)
dd = datetime.date(datey, datem, dated)
print(dd - delta)
print(dd)
