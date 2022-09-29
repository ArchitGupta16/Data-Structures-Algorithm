def matrix_multiplication(x, y,r1,c1,r2,c2):
    if c1 == r2:
        z = [[0 for i in range(c2)] for j in range(r1)]
        for i in range(0, r1):
            for j in range(0, c2):
                for k in range(0, r2):
                    z[i][j] = z[i][j] + x[i][k] * y[k][j]
                    return(z)

    else:
        print("multiplication not possible!!!")

r1=int(input("enter number of rows of matrix one:"))
c1=int(input("enter number of columns of matrix one:"))
r2=int(input("enter number of rows of matrix two:"))
c2=int(input("enter number of columns of matrix two:"))

x=[ [ 0 for i in range(c1) ] for j in range(r1) ]
y=[ [ 0 for i in range(c2) ] for j in range(r2) ]
print(x,y)
for i in range(0, r1):
    for j in range(0, c1):
        x[i][j]=int(input(f"Enter values of matrix 1 {[i]}{[j]}:"))


for i in range(0, r2):
    for j in range(0, c2):
        y[i][j]=int(input(f"Enter values of matrix 2 {[i]}{[j]}:"))


print(matrix_multiplication(x,y,r1,c1,r2,c2))
