m1,m2,m3,m4 = map(int,input().split())

total = m1+m2+m3+m4
print(f"{total}")

percentage = total/4
print(f"{percentage:.2f}")

if (percentage > 75 ) :
	print("Distinction")
elif (percentage >= 60 and percentage <75) :
	print("First Division")
elif (percentage >= 50 and percentage < 60) :
	print("Second Division")
elif (percentage >= 40 and percentage < 50) :
	print("Third Division")
else :
	print("Fail")
