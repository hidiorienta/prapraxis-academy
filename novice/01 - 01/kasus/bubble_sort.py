list = [-2, -5, -7, -1, 0, -12, 6, 101, 10, 80, 45, 70]

for i in range(len(list)-1, 0, -1):
  for j in range(i):
    if list[j] > list[j+1]:
      t=list[j]
      list[j]=list[j+1]
      list[j+1]=t
print(list)
    
