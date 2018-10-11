# Roll no.:
# Registration no.:
# Create a list of prime factors of a given number.

from q10 import isPrime
n = int(input("Enter number: "))

factor_list = []
for i in range(1, n+1):
	if n % i == 0 and isPrime(i):
		factor_list.append(i)
print(factor_list)

# EXECUTION:
# Enter number: 360
# [2, 3, 5]
#
# Enter number: 2310
# [2, 3, 5, 7, 11]
#
# Enter number: 7
# [7]