import random
def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
x = int(input("Enter x:"))
arr = [random.randrange(1,100) for i in range(x)]
print(arr)
insertionsort(arr)
print("Sorted Array:")
print(arr)
