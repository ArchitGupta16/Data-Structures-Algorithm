lb=0
pos=-1

size_arr=int(input("Enter a length of sorted array:"))
arr=[0]*size_arr
arr=[None]*size_arr

#for input of array
for i in range(0,size_arr):
    input_array=int(input(f"Enter array value {i+1}:"))
    arr[i]=input_array
print(arr)

val=int(input("Enter value to search:"))

ub=size_arr

#binary search
def Binary_search(arr,lb,ub,val):
    mid=(ub+lb)//2
    if arr[mid]==val:
        print(f"element found!! at {mid}")

    elif arr[mid]>val:
        Binary_search(arr,lb,mid-1,val)

    elif val>arr[mid]:
        Binary_search(arr,mid+1,ub,val)

    else:
        print("Element not found")

a=Binary_search(arr,lb,ub,val)
print(a)


