def sum_of_digits_recursive(n):
	if n==0:
		return 0
	else:
		return(n %10) + sum_of_digits_recursive(n // 10)

number = int(input())
result = sum_of_digits_recursive(number)	
print(result)
