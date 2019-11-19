persons = [
  { "name": 'Peter', "age": 16 },
  { "name": 'Mark', "age": 18 },
  { "name": 'John', "age": 27 },
  { "name": 'Jane', "age": 14 },
  { "name": 'Tony', "age": 24},
]
fullAge = []
for i in range(len(persons)):
    if persons[i]["age"] >= 18:
        fullAge.append(persons[i])
        i += 1

print(fullAge)