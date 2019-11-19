arr1 = [1, 2, 3]
arr2 = []
for i in range(len(arr1)):
    arr2.append(arr1[i] * 2)
    i += 1
# prints [ 2, 4, 6 ]
print(arr2)


birthYear = [1975, 1997, 2002, 1995, 1985]
ages = []
for i in range(len(birthYear)):
    age = 2018 - birthYear[i]
    ages.append(age)
# prints [ 43, 21, 16, 23, 33 ]
print(ages)

for i, z in enumerate(birthYear):
    print(i+1, z)