
#Ascending Order
def bubble(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1]= arr[i+1],arr[i]
    return arr

#Descending Order
def bubble2(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i]<arr[i+1]:
                arr[i], arr[i+1]= arr[i+1],arr[i]
                print(arr)
            else:
                print(arr)
        print("\n")
    return arr

arr = [53, 20, 3, 10, 77, 20]
print(bubble2(arr))