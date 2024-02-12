def selectionSort(arr):
    
    n = len(arr)
    
    for i in range(0,n-1):
        min_idx = i
        for j in range(i,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


temp = input("Enter numbers separated by a comma:\n").strip()
arr = [int(item) for item in temp.split(",")]
selectionSort(arr)
print(arr)
