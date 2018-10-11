# Roll number:
# Registration number:
# To verify the Goldbach conjecture and find the Goldbach composition of 1st n even numbers.

from q11 import prime_list

def goldbach_comp(n):
	lst = prime_list(1, n)
	for i in range(len(lst)):
		for j in range(i, len(lst)):
			if lst[i] + lst[j] == n:
				print(n, "=", lst[i], "+", lst[j])

if __name__ == "__main__":
	n = int(input("Enter limit: "))
	for i in range(1, n+1):
		goldbach_comp(2*i)

# EXECUTION
# Enter limit: 10
# 4 = 2 + 2
# 6 = 3 + 3
# 8 = 3 + 5
# 10 = 3 + 7
# 10 = 5 + 5
# 12 = 5 + 7
# 14 = 3 + 11
# 14 = 7 + 7
# 16 = 3 + 13
# 16 = 5 + 11
# 18 = 5 + 13
# 18 = 7 + 11
# 20 = 3 + 17
# 20 = 7 + 13
