def Bubble_sort_asc(x,size):
    if choice==1:
        count=0
        for i in range(0,size):
            for j in range(0,size-i-1):
                if x[j]>x[j+1]:
                    count += 1
                    temp=x[j+1]
                    x[j+1]=x[j]
                    x[j]=temp

        if count==0:
            print("Best case....array already sorted")
        if count==size:
            print("Worst case...array reverse sorted")
    return(x)

def Bubble_sort_dsc(x,size):
    if choice==2:
        count=0
        for i in range(0,size):
            for j in range(0,size-i-1):
                if x[j]<x[j+1]:
                    count+=1
                    temp=x[j]
                    x[j]=x[j+1]
                    x[j+1]=temp

        if count == 0:
            print ("Best case....array already sorted")
        if count == size:
            print ("Worst case...array reverse sorted")
    return(x)

def insertion_sort_asc(x,size):
    if choice==3:
        count=0
        for i in range (1,size):
            key=x[i]
            j=i-1
            while j>=0 and key<x[j]:
                count+=1
                x[j+1]=x[j]
                j-=1
            x[j+1]=key

        if count == 0:
            print("Best case....array already sorted")
        if count == size:
            print ("Worst case...array reverse sorted")
    return(x)

def insertion_sort_dsc(x,size):
    if choice==4:
        count=0
        for i in range (1,size):
            key=x[i]
            j=i-1
            while j>=0 and key>x[j]:
                count+=1
                x[j+1]=x[j]
                j-=1
            x[j+1]=key

        if count == 0:
            print ("Best case....array already sorted")
        if count == size:
            print ("Worst case...array reverse sorted")
    return(x)

def Selection_sort_asc(x,size):
    if choice==5:
        count=0
        for i in range (0,size):
            min=i
            for j in range (i+1,size):
                if x[j]<x[min]:
                    min=j
            if x[i]>x[min]:
                count+=1
                temp=x[min]
                x[min]=x[i]
                x[i]=temp

        if count == 0:
            print ("Best case....array already sorted")
        if count+1 == size:
            print ("Worst case...array reverse sorted")
    return(x)

def Selection_sort_dsc(x,size):
    if choice==6:
        count=0
        for i in range (0,size):
            min=i
            for j in range (i+1,size):
                if x[j]>x[min]:
                    min=j
                    count += 1
            if x[i]<x[min]:

                temp=x[min]
                x[min]=x[i]
                x[i]=temp
        print(count)

        if count == 0:
            print ("Best case....array already sorted")
        if count+1 == size:
            print ("Worst case...array reverse sorted")
    return(x)

choice=int(input("MENU:\n"
                 "1. Bubble sort ascending \n"
                 "2. Bubble sort descending \n"
                 "3. insertion sort ascending \n"
                 "4. Insertion sort descending \n"
                 "5. Selection sort ascending \n"
                 "6. Selection sort descending \n"
                 "7. Exit"))

size=int(input("enter size:"))
x=[0]*size
for i in range(0,size):
    x[i]=int(input("Enter values of array:"))

if choice==1:
    print(Bubble_sort_asc(x,size))
if choice==2:
    print(Bubble_sort_dsc(x,size))
if choice==3:
    print(insertion_sort_asc(x,size))
if choice==4:
    print(insertion_sort_dsc(x,size))
if choice==5:
    print(Selection_sort_asc(x,size))
if choice==6:
    print(Selection_sort_dsc(x,size))
if choice==7:
    print("Enter a valid option!!!")