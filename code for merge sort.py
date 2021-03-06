import random
def Merge(p,r):
    result = []  
    i,j = 0,0
    while i<len(p) and j<len(r):
        if p[i] <= r[j]:
            result.append(p[i]) 
            i+=1
        else:
            result.append(r[j])  
            j+=1
    result += p[i:]
    result += r[j:]
    return result
def MergeSort(arr):
    if(len(arr)<= 1): 
        return arr
    q = int(len(arr)/2)
    p = MergeSort(arr[:q])
    r = MergeSort(arr[q:])
    return Merge(p,r) 
n = int(input("enter n:"))
arr = [random.randrange(1,100) for i in range(n)]
print("Original array:")
print(arr)
print("Sorted array:")
print(MergeSort(arr))
