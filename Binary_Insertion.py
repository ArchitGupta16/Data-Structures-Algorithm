size_arr=int(input("Enter size of array:"))
arr=[None]*size_arr
n_elements=0
location=0
val_after=0
choice=1

#linear search
def linear_search(arr,val_aft):
    for i in range(len(arr)):
        if arr[i]==val_aft:
            location=i
            print("location of the entered element is:",location)
            return location

#menu driven
while(choice in range (0,5)):
    val = int(input("Enter value to be inserted:"))
    choice = int(input('''Enter 1 for insertion at end,
2 for insertion in beginning , 
3 for insertion at a location ,
4 for insertion after a value 
otherwise exit!!!'''))

    if n_elements>size_arr:
        print("Array Overflow!!")


    if (choice==1):
        arr[n_elements]=val
        n_elements+=1
        print(arr)


    if (choice==2):
        i=1
        while(i<=n_elements):
            arr[i]=arr[i-1]
            i=i+1
        arr[0]=val
        n_elements+=1
        print(arr)

    if (choice==3):
        loc=int(input("Enter the index where you want to insert:"))
        i=n_elements
        while(i>loc):
            arr[i]=arr[i-1]
            i-=1

        arr[loc]=val
        print(arr)
        n_elements+=1

    if (choice==4):
        val_after=int(input("Enter the value after you want to insert:"))
        locc=linear_search(arr,val_after)
        i=locc+1
        while(i<n_elements):
            arr[i+1]=arr[i]
            i=i+1
        arr[locc+1]=val
        print(arr)
        n_elements+=1











