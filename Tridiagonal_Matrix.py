size=int(input("Enter size:"))

A=[ [ 0 for i in range(size) ] for j in range(size) ]

def tridiagonalmatrix(A):
	if size>=3:
		for i in range (0,size):
			for j in range (0,size):
				if abs(i-j)>1:
					A[i][j]=0
				else:
					x=int(input(f"value [{i}][{j}]:"))
					A[i][j]=x
		for i in A:
			print (i)
	else:
		print("minimum 3x3 matrix required!!!")

tridiagonalmatrix(A)