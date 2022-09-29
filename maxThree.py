def max_three(a,b,c):
    if a==b==c:
        print("all are equal")
    elif b==c and b>a:
        print('b and c are equal and largest')
    elif a==b and a>c:
        print("a and b are equal and largest")
    elif a==c and a>b:
        print("a and c are equal and largest")
    elif a>b and a>c:
        print("a is largest")
    elif b>c and b>c:
        print("b is largest")
    else:
        print("c is largest")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
max_three(x,y,z)