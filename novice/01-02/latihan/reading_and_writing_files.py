f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# value = ('the answer', 42)
# s = str(value)  # convert the tuple to string
# f.write(s)

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))

print(f.seek(5))

print(f.read(1))

print(f.seek(-3, 2))

print(f.read(1))