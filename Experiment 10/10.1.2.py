def reverse_string(str1):
	res = ""
	ln = len(str1)
	for i in range(ln-1, -1, -1):
		res = res + str1[i]
	return res
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}"
