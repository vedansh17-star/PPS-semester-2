date = int (input())
month = int (input())
year = int (input())

flag = True
if (year<0 or month<0 or month>12):
	flag = False
if month in (1,3,5,7,8,10,12):
	maxdays=31
elif month in (4,6,9,11):
	maxdays=30
else:
	if year % 4 == 0:
		maxdays=29
	else:
		maxdays=28
if date>maxdays:
	flag=False

date = date + 1
if date>maxdays:
	date=1
	month = month +1

if month > 12:
	month = 1
	year= year +1

if flag:
	print(f"{date:02d}-{month:02d}-{year:d}")
else:
	print("Invalid Date")
