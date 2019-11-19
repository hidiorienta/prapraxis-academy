def power(base, exp):
     return base ** exp
cube = partial(power, exp=3)
print(cube(5))  # returns 125