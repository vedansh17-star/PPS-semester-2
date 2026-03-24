A = set(map(int, input("Set A: ").split()))
B = set(map(int, input("Set B: ").split()))

union_set = A | B
intersection_set = A & B
difference_set = A - B

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
