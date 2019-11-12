# input as flat text
a =  { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

# the same input can also be read from a file
a = open('/Documents/praxis-academy/novice/01-05/latihan/file.py', 'r')

# returns a printable representation of the input;
# the output can be written to a file as well
print(repr(a))

# write content to files using repr
with open('/Documents/praxis-academy/novice/01-05/latihan/file.py') as f:f.write(repr(a))
