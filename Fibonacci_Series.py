
no_of_terms=int(input("enter number of terms to be printed in series:"))


def fibonacci_ser(num):
    n1 = 0
    n2 = 1
    count = 0
    if num<=0:
        print("Enter new positive integer")
    if num==1:
        print("Fibonacci series upto",num,n1)
    elif num==2:
        print("Fibonacci series upto",num,n1,n2)
    else:
        while count<num:
            print(n1)
            next_term=n1+n2
            n1=n2
            n2=next_term
            count+=1

fibonacci_ser(no_of_terms)