str = input()

count = 0
for i in str:
	if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
		count += 1

print(count)
