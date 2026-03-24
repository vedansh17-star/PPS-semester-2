st = input()

l = len(st)
flag = True
for i in range(l):
	if st[i] != st[l-1-i]:
		flag = False
if flag:
	print("Palindrome")
else:
	print("Not a Palindrome")
