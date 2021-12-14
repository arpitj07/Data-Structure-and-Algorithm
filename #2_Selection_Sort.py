#for non duplicate values
def selection(arr):
	# ascending sorting
    for i in range(len(arr)-1):
        minval = min(arr[i:])   # use max() for descending sorting
        minind = arr.index(minval)
        arr[i], arr[minind] = arr[minind], arr[i]
    return arr


# without inbuilt min-max methods
def selection2(arr):

    for i in range(len(arr)-1):
        minval = arr[i]
        
        for j in range(i+1,len(arr)):
            if minval > arr[j]:
                minval = arr[j] 

        minind = arr.index(minval,i)
        if arr[i] != arr[minind]:
            arr[i], arr[minind] = arr[minind], arr[i]
    return arr 



def selection3(arr):

    for i in range(len(arr)-1):
        m_ind =i
        
        for j in range(i+1,len(arr)):
            if arr[m_ind] < arr[j]:
                m_ind = j 

        if arr[i] != arr[m_ind]:
            arr[i], arr[m_ind] = arr[m_ind], arr[i]
    return arr 


arr = [53, 20, 3, 10, 77, 20]
print(selection3(arr))