str = ""
st = input()

for i in st:
	if i.isalnum() or i.isspace():
		str = str + i
print(str)
