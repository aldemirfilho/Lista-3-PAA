flips = 0

def flip(arr, i):
    start = 0
    global flips
    if start < i:
         flips += 1
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1

def findMax(arr, n):
    max_i = 0
    for i in range (0,n):
        if arr[i] > arr[max_i]:
            max_i = i
    return max_i

def pancakeSort(arr, n, no):
    curr_size = n
    if curr_size < 1:
        return
   
    max_i = findMax(arr, curr_size)

    if max_i != curr_size - 1:
        printArray(arr,no)
        print("\n")
       
        flip(arr, max_i)
       
        printArray(arr,no)
        print("\n")
        
        print('Flip geral: ')
        flip(arr, curr_size-1)
        
        printArray(arr,no)
        print("\n")

        
        
    
    pancakeSort(arr,curr_size-1,no)

def printArray(arr,n):
    for i in range(0,n):
        print ("%d"%( arr[i]),end=" ")

arr = [0, 9, 1, 8, 2, 7, 3, 6, 5, 4]
#arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancakeSort(arr, n, n)
print ("Sorted Array ")
printArray(arr,n)
print("\nFlips = ", flips)
