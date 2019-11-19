import functools

arr = [5, 7, 1, 8, 4]
sum1 = functools.reduce(lambda a,b : a+b,arr)
sum2 = sum1+10
# max = functools.reduce (lambda a,b : a if a > b else b,arr)

# print 25
print(sum1)
# print 35
print(sum2)