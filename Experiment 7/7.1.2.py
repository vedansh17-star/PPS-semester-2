a,b,c = input().split()
digits = [a,b,c]

for i in range(3):
	for j in range(3):
		for k in range(3):
			if(i!=j and i!=k and j!=k):
				print(digits[i] + digits[j] + digits[k])
