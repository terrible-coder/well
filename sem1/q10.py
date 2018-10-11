# Roll no.:
# Registration no.:
# Check whether a particular number is prime or not.

from math import sqrt

def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

if __name__ == "__main__":
	n = int(input("Enter number to check: "))
	if isPrime(n):
		print(n, "is prime.")
	else:
		print(n, "is not prime.")

# EXECUTION:
# Enter number to check: 15
# 15 is not prime.
#
# Enter number to check: 121
# 121 is not prime.
#
# Enter number to check: 127
# 127 is prime.