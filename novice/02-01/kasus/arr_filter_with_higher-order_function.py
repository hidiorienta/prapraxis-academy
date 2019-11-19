persons = [
  { "name": 'Peter', "age": 16 },
  { "name": 'Mark', "age": 18 },
  { "name": 'John', "age": 27 },
  { "name": 'Jane', "age": 14 },
  { "name": 'Tony', "age": 24},
]
fullAge = map(lambda x["age"]: 18 >= x["age"], persons)

print(fullAge)