def arr(x):
    return x * 2

arr1 = [1, 2, 3]
arr2 = map(arr, arr1)

print(list(arr2))


arr1 = (1, 2, 3)
arr2 = map(lambda x: x*2, arr1)
print(list(arr2))


birthYear = [1975, 1997, 2002, 1995, 1985]
ages = map(lambda x: 2018-x, birthYear)
# prints [ 43, 21, 16, 23, 33 ]
print(list(ages))