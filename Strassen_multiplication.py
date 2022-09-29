"""
Strassen_multiplication(A,B)

step1. n = A.rows

step2. C = nxn matrix

step3. if n==1 then
            C[0][0] = A[0][0] * B[0][0]

       else divide a, b and c
            C11 = Strassen_multiplication(A11,B11) + Strassen_multiplication(A12,B21)
            C12 = Strassen_multiplication(A11,B12) + Strassen_multiplication(A12,B21)
            c21 = Strassen_multiplication(A11,B11) + Strassen_multiplication(A21,B12)
            c22 = Strassen_multiplication(A21,B11) + Strassen_multiplication(A22,B22)
       EndIf
       return C

Step4. Exit
"""


def add_matrix(z, x, y, r3, c3):
    n = len(x[0])
    for i in range(0, n):
        for j in range(0, n):
            z[i + r3][j + c3] = x[i][j] + y[i][j]


def strassen_mul(x, y, r1, c1, r2, c2, size):
    c = [[0 for i in range(size)] for j in range(size)]

    if size == 1:
        c[0][0] = x[0][0] * y[0][0]


    else:
        newsize = size // 2
        add_matrix(c, strassen_mul(x, y, r1, c1, r2, c2, newsize),
                   strassen_mul(x, y, r1, c1 + newsize, r2 + newsize, c2, newsize),
                   0, 0)

        add_matrix(c, strassen_mul(x, y, r1, c1, r2, c2 + newsize, newsize),
                   strassen_mul(x, y, r1, c1 + newsize, r2 + newsize, c2 + newsize, newsize),
                   0, newsize)

        add_matrix(c, strassen_mul(x, y, r1 + newsize, c1, r2, c2, newsize),
                   strassen_mul(x, y, r1 + newsize, c1 + newsize, r2 + newsize, c2, newsize),
                   newsize, 0)

        add_matrix(c, strassen_mul(x, y, r1 + newsize, c1, r2, c2 + newsize, newsize),
                   strassen_mul(x, y, r1 + newsize, c1 + newsize, r2 + newsize, c2 + newsize, newsize),
                   newsize, newsize)
    return (c)


r1 = int(input("enter number of rows of matrix one:"))
c1 = int(input("enter number of columns of matrix one:"))
r2 = int(input("enter number of rows of matrix two:"))
c2 = int(input("enter number of columns of matrix two:"))
size = r1

x = [[0 for i in range(c1)] for j in range(r1)]
y = [[0 for i in range(c2)] for j in range(r2)]
print(x, y)
for i in range(0, r1):
    for j in range(0, c1):
        x[i][j] = int(input(f"Enter values of matrix 1 {[i]}{[j]}:"))

for i in range(0, r2):
    for j in range(0, c2):
        y[i][j] = int(input(f"Enter values of matrix 2 {[i]}{[j]}:"))

print(strassen_mul(x, y, r1, c1, r2, c2, size))
