size_arr=int(input("Enter size of array:"))
arr=[None]*size_arr
n_elements=0
val_after=0
choice=1

#INPUT ARRAY
for i in range(0,size_arr):
    input_array=int(input(f"Enter array value {i+1}:"))
    arr[i]=input_array
    n_elements+=1
print(arr,n_elements)

#LINEAR SEARCH
def linear_search(arr,val_aft):
    for i in range(len(arr)):
        if arr[i]==val_aft:
            location=i
            print("location of the entered element is:",location)
            return location

while(choice in range (0,5)):

#MENU DRIVEN
    choice = int(input('''Enter 1 for delete at end,
2 for delete in beginning , 
3 for delete at a location ,
4 for delete after a value 
otherwise exit!!!'''))

    if (choice==1):
        arr[n_elements-1]=None
        n_elements-=1
        print(arr)

    if (choice==2):
        i=1
        while(i<n_elements):
            arr[i-1]=arr[i]
            i=i+1
        arr[n_elements-1]=None
        n_elements-=1
        print(arr)

    if (choice==3):
        locc=int(input("Enter the index where you want to delete:"))
        i=locc+1
        while(i<n_elements):
            arr[i-1]=arr[i]
            i+=1
        arr[n_elements-1]=None
        print(arr)
        n_elements-= 1

    if (choice == 4):
        val_after = int(input("Enter the value after you want to delete:"))
        locc = linear_search(arr, val_after)
        i=locc+1
        while (i<=n_elements-1):
            arr[i-1] = arr[i]
            i=i+1
        arr[n_elements-1]=None
        print(arr)
        n_elements -= 1


