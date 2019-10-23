list = [-2, -5, -7, -1, 0, -12, 6, 101, 10, 80, 45, 70]
def mergesort(list):
    n=len(list)
    if n<2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]
 
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i< len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            list[k]=right[j]
            j=j+1
            k=k+1
mergesort(list)
print(list)
