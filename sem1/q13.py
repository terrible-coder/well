# Roll no.:
# Registration no.:
# Calculate the greatest common divisor of two numners.

def gcd(a, b):
	if a > b:
		m = a
		n = b
	else:
		m = b
		n = a
	for i in range(n, 0, -1):
		if m % i == 0 and n % i == 0:
			return i
			
if __name__ == "__main__":
	a = int(input("Enter 1st number: "))
	b = int(input("Enter 2nd number: "))
	print("GCD =", gcd(a, b))

# EXECUTION
# Enter 1st number: 18
# Enter 2nd number: 24
# GCD = 6
#
# Enter 1st number: 19
# Enter 2nd number: 76
# GCD = 19