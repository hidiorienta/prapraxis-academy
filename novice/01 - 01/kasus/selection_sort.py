list = [-2, -5, -7, -1, 0, -12, 6, 101, 10, 80, 45, 70]

def SelectionSort(list):
   for i in range(len(list)-1,0,-1):
       Max=0
       for j in range(1,i+1):
           if list[j]>list[Max]:
               Max = j
 
       t = list[i]
       list[i] = list[Max]
       list[Max] = t
SelectionSort(list)
print(list)