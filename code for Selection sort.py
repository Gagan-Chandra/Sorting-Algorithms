import random
def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        minv = i
        for j in range(i+1,n):
            if arr[j] < arr[minv]:
                minv = j
        if minv != i:
            temp = arr[i]
            arr[i] = arr[minv]
            arr[minv] = temp
    return arr
x = int(input("Enter x:"))
arr = [random.randrange(1,100) for i in range(x)]
print(arr)
print("Sorted Array:")
print(selectionsort(arr))
