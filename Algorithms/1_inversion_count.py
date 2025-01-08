#For each element count the number of elements which are on the right side of it which are smaller than it 


def getInverseCountsBruteForce(arr):
    n = len(arr)
    inv_count = 0 
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i] > arr[j]):
                inv_count+=1
    return inv_count;

# print(getInverseCountsBruteForce([1,5,2, 8,3,4]))



#The below method is done by following the merge sort algorithm 
#Algorithm 
# 1. Find the middle point to divide the array into 2 halves . middle = (l+r)/2
# 2. Call mergesort for the first half . mergesort(arr,l,m)
# 3. Call mergesort fir the second half mergesort(arr,m+l,r)
# 4. Merge the 2 halves sorted in step 2 and 3 merge(arr,l,m,r)


def mergeSort(arr):
    n = len(arr)
    temp_arr = [0]*n
    return _mergeSort(arr,temp_arr,0,n-1)


def _mergeSort(arr,temp_arr,left,right):
    inv_count = 0 
    if(right > left):
        mid = ( left + right )//2
        inv_count += _mergeSort(arr,temp_arr,left,mid)
        inv_count += _mergeSort(arr,temp_arr,mid+1,right)
        inv_count += merge(arr,temp_arr,left,mid,right)
    return inv_count

def merge(arr,temp_arr,left,mid,right):
    i = left 
    j = mid+1
    k = left 
    inv_count = 0 
    while(i <= mid and j<= right):
        if(arr[i]<=arr[j]):
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            k+=1
            j+=1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    
    return inv_count

        
arr = [1, 20, 6, 4, 5]
result = mergeSort(arr)
print("Number of inversions are", result)