a, b, c = map(int,input() .split())
d = ( b * b ) - 4 * a * c
sqrd = d ** 0.5

if d > 0:
	root1 = (-b + sqrd) / (2 * a)
	root2 = (-b - sqrd) / (2 * a)
	print(f"root1 = {root1:.2f}")
	print(f"root2 = {root2:.2f}")

elif d == 0:
	root = -b / (2 * a)
	print(f"root1 = root2 = {root:.2f}")

else:
	real_part =(-b) / (2 * a)
	imaginary_part = sqrd / (2 * a)
	print(f"root1 = {real_part.real:.2f}+{imaginary_part.imag:.2f}i")
	print(f"root2 = {real_part.real:.2f}-{imaginary_part.imag:.2f}i")
