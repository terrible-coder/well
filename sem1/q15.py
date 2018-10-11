# Roll no.:
# Registration no.:
# Evaluate fibonacci numbers and calculate the limit of the numbers.

def fibo(n):
	"""Returns nth fibonacci number."""
	a, b = 0, 1
	for i in range(1, n):
		a, b = b, a+b
	return b

def calc_ratio():
	"""Calculates the limit of the ratio of fibonacci numbers correct to 4th decimal place."""
	c, d = 1, 1
	while True:
		phi = d / c
		c, d = d, c+d
		phi1 = d / c
		if abs(phi1 - phi) < 1.0e-5:
			return phi

if __name__ == "__main__":
	n = int(input("Enter limit: "))
	print([fibo(i) for i in range(1, n+1)])
	print("Limit =", calc_ratio())

# EXECUTION
# Enter limit: 10
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Limit = 1.6180371352785146
