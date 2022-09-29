def prime_number(x):
    if x>1:
        for i in range (2,x//2):
            if x%i==0:
                print("not a prime number")
                break
        else:
            print("prime number")

prime_number(8)
