# Ascedning Order
def insertion(arr):
    
    for i in range(1,len(arr)):
        curr_element = arr[i]
        pos = i
        for j in reversed(range(i)):
            
            if curr_element < arr[j]:
                # arr[i],arr[j] = arr[j], arr[i]
                arr[i] = arr[j]
                pos = j
        arr[pos] = curr_element
                
                
        #     print(j, end=',')
        # print("\n")
    return arr

# Descending Order


arr = [53, 20, 3, 10, 77, 20]
print(insertion(arr))
