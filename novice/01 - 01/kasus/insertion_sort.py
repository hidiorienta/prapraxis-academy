list = [-2, -5, -7, -1, 0, -12, 6, 101, 10, 80, 45, 70]
def InsertionSort(list):
   for i in range(1,len(list)):
 
     valueaktif = list[i]
     posisi = i
 
     while posisi>0 and list[posisi-1]>valueaktif:
         list[posisi]=list[posisi-1]
         posisi = posisi-1
 
     list[posisi]=valueaktif
InsertionSort(list)
print(list)