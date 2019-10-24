list = [-2, -5, -7, -1, 0, -12, 6, 101, 10, 80, 45, 70]
def quickshort(list,start,end):
    if start<end:
        pindex = partition(list,start,end)
        quickshort(list,start,pindex-1)
        quickshort(list,pindex+1,end)
 
def partition(list,start,end):
    pivot = list[end]
    pindex = start-1
    for i in range(start,end):
        if list[i]<=pivot:
            pindex = pindex + 1
            list[pindex],list[i]=list[i],list[pindex]
    list[pindex+1],list[end]=list[end],list[pindex+1]
    return pindex+1
quickshort(list,0,len(list)-1)
print(list)