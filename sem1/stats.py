# Roll number:
# Registration number:
# Calculate the mean, median and mode of a list of numbers.

def mean(a):
	"""Calculates and returns the mean of a list of numbers.
		a - list to calculate mean of"""
	return sum(a) / len(a)

def median(a):
	"""Calculates and returns the median of a list of numbers.
		 a - list to calculate median of"""
	b = sorted(a)
	n = len(b)
	if n % 2 == 0:
		return (b[n//2-1] + b[n//2]) / 2
	return b[n//2]

def freq(a):
	"""Determines the distinct elements in a list.
		 Returns a list of distinct elements and corresponding frequencies."""
	items = []
	for item in a:
		if not item in items:
			items.append(item)
	f = []
	for item in items:
		c = 0
		for elt in a:
			if item == elt:
				c += 1
		f.append(c)
	return items, f

def mode(a):
	"""Calculates and returns the mode of a list of numbers.
		 a - list to calculate mode of"""
	i, f = freq(a)
	return i[f.index(max(f))]

if __name__ == "__main__":
	i, a = 0, []
	print("Enter data elements (enter nothing when you want to stop input).")
	while True:
		st = (input(str(i+1)+": "))
		if st == "":
			break
		a.append(int(st))
		i += 1
	print()
	print("Entered data:", a)
	print("Mean =", mean(a))
	print("Median =", median(a))
	print("Mode =", mode(a))

# EXECUTION
# Enter data elements (enter nothing when you want to stop input).
# 1: 243798
# 2: 14698
# 3: 97979797
# 4: 987       
# 5: 9022        
# 6: 769092
# 7: 100
# 8: 
# 
# Entered data: [243798, 14698, 97979797, 987, 9022, 769092, 100]
# Mean = 14145356.285714285
# Median = 14698
# Mode = 243798