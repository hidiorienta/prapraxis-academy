strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']
def mapForEach(arr, fn):
    newArray = []
    for i in range(0,len(strArray)):
        newArray.append(fn(arr[i]))
        i += 1
    return newArray

lenArray = mapForEach(strArray,len)

# print [ 10, 6, 3, 4, 1 ]
print(lenArray)