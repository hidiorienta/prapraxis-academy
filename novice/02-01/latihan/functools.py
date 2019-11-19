val = [1, 2, 3, 4, 5, 6]

# Multiply every item by two
list(map(lambda x: x * 2, val)) # [2, 4, 6, 8, 10, 12]
# Take the factorial by multiplying the value so far to the next item
reduce(lambda: x, y / x * y, val, 1) # 1 * 1 * 2 * 3 * 4 * 5 * 6

print(reduce)