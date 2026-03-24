n = int(input("dimension: "))
A = []
print("first matrix:")
for i in range(n):
	row = list(map(int, input().split()))
	A.append(row)

B = []
print("second matrix:")
for i in range(n):
	row = list(map(int,input().split()))
	
	B.append(row)

result = [[0]*n for i in range(n)]

for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for i in range(n):
	for j in range(n):
		if j == n-1:
			print(result[i][j], end="")
		else:
			print(result[i][j], end=" ")
	print()
