import random
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
x = int(input("Enter value of x:"))
arr =[random.randrange(1,100) for i in range(x)]
print(arr)
bubblesort(arr)
print("Sorted Array:")
print(arr)
