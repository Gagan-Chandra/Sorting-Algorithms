import random
def Quicksort(a,p,r):
    if p<=r:
        q = partition(a,p,r)
        Quicksort(a,p,q-1)
        Quicksort(a,q+1,r)
        return a
def partition(a,p,r):
    i = p - 1
    x = a[r]
    for j in range(p,r):
        if a[j] <= x:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return (i+1)
n = int(input("enter n:"))
arr = [random.randrange(1,100) for i in range(n)]
print("Original array:")
print(arr)
print("Sorted array:")
arr2 = Quicksort(arr,0,n-1)
print(arr2)
