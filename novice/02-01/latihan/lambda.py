(lambda a, b: a + b)(3, 4)  # returns 7

addition = lambda a, b: a + b
print(addition(3, 4))  # returns 7


authors = ['Octavia Butler', 'Isaac Asimov', 'Neal Stephenson', 'Margaret Atwood', 'Usula K Le Guin', 'Ray Bradbury']
sorted(authors, key=len)  # Returns list ordered by length of author name
print(sorted(authors, key=lambda name: name.split()[-1]))  # Returns list ordered alphabetically by last name.