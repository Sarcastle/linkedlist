def insertionSort(arr):
    n = len(arr)  # gets length of array
      
    if n <= 1:
        return  # if array has 0 or 1 it returns because it is already sorted
    for i in range(1, n):  # iterates from array starting at second element 
        key = arr[i] # stores the current element as the key 
        j = i-1
        while j >= 0 and key < arr[j]:  # elements greater than the key move one postion to the right
            arr[j+1] = arr[j]  # shifts elements to the right
            j -= 1
        arr[j+1] = key  # places the key in the correct position
  
# sorts the array
arr = [15, 4, 9, 20, 17]
insertionSort(arr)
print(arr)
