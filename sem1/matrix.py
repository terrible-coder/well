# Roll no.:
# Registration no.:
# Matrix algebra

def transpose(A):
	m, n = len(A), len(A[0])
	return [[A[i][j] for i in range(m)] for j in range(n)]

def add(A, B):
	m, n = len(A), len(A[0])
	return [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

def subtract(A, B):
	m, n = len(A), len(A[0])
	return [[A[i][j] - B[i][j] for j in range(n)] for i in range(m)]

def multiply(A, B):
	m, n = len(A), len(B[0])
	p = len(B)
	return [[sum([A[i][k]*B[k][j] for k in range(p)]) for j in range(n)] for i in range(m)]

def commutator(A, B):
	C = multiply(A, B)
	D = multiply(B, A)
	return subtract(C, D)

def anti_commutator(A, B):
	C = multiply(A, B)
	D = multiply(B, A)
	return add(A, B)

def display(A):
	for row in A:
		for x in row:
			print(x, end="\t")
		print()

def createMatrix(m, n):
	return [[None for j in range(n)] for i in range(m)]

def fillMatrix(A):
	m, n = len(A), len(A[0])
	for i in range(m):
		print("Enter data for row", str(i+1), ":")
		for j in range(n):
			A[i][j] = float(input(""))

if __name__ == "__main__":
	m = int(input("Enter no. of rows of matrix A: "))
	n = int(input("Enter no. of columns of matrix A: "))
	A = createMatrix(m,n)
	fillMatrix(A)
	m = int(input("Enter no. of rows of matrix B: "))
	n = int(input("Enter no. of columns of matrix B: "))
	B = createMatrix(m,n)
	fillMatrix(B)
	print("\nEntered data:\nMatrix A:")
	display(A)
	print("Matrix B:")
	display(B)
	print("\nTranspose of A:")
	display(transpose(A))
	print("\nA+B =")
	display(add(A, B))
	print("\nA-B =")
	display(subtract(A, B))
	print("\nAB =")
	display(multiply(A, B))
	print("\n[A,B] =")
	display(commutator(A, B))
	print("\n{A,B} =")
	display(anti_commutator(A, B))

# EXECUTION:
# Enter no. of rows of matrix A: 2
# Enter no. of columns of matrix A: 2
# Enter data for row 1 :
# 1
# 1
# Enter data for row 2 :
# 0
# 1
# Enter no. of rows of matrix B: 2
# Enter no. of columns of matrix B: 2
# Enter data for row 1 :
# 5
# 0
# Enter data for row 2 :
# 0
# 5
#
# Entered data:
# Matrix A:
# 1.0     1.0
# 0.0     1.0
# Matrix B:
# 5.0     0.0
# 0.0     5.0
#
# Transpose of A:
# 1.0     0.0
# 1.0     1.0
#
# A+B =
# 6.0     1.0
# 0.0     6.0
#
# A-B =
# -4.0    1.0
# 0.0     -4.0
#
# AB =
# 5.0     5.0
# 0.0     5.0
#
# [A,B] =
# 0.0     0.0
# 0.0     0.0
#
# {A,B} =
# 6.0     1.0
# 0.0     6.0
