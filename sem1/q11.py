# Roll no.:
# Registration no.:
# Create a list of prime numbers between two given numbers.

from q10 import isPrime

def prime_list(a, b):
	lst = []
	for i in range(a, b):
		if isPrime(i):
			lst.append(i)
	return lst

if __name__ == "__main__":
	a = int(input("Enter starting point: "))
	b = int(input("Enter ending point: "))
	print(prime_list(a, b))

# EXECUTION:
# Enter starting point: 10
# Enter ending point: 80
# [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]