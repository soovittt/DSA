#This algorithm uses the pivot element to divide the arrays and sorts it recursively 

def partition(array,low,high):
    #This takes the last element as the pivot 
    pivot = array[high]
    #this chooses i 
    i = low - 1 
    #loops through the array and try to swap the elements to maintain correct positon
    for j in range(low , high):
        if(array[j] <= pivot):
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high], array[i+1]
    return i+1



#The recursive algorithm which will call itself to apply quicksort 
def quicksort(array,low,high):
    #checking if high is None
    if high is None:
        return len(array)-1
    
    #chekcing if low <  high 
    if(low<high):
        #calculate the pivot 
        pivot = partition(array,low,high)
        #quicksort the left partition
        quicksort(array,low,pivot-1)
        #quicksort the right partititon
        quicksort(array,pivot+1,high)
    

array = [10, 7, 8, 9, 1, 5]
N = len(array)
quicksort(array, 0, N - 1)
print('Sorted array:')
for x in array:
    print(x, end=" ")