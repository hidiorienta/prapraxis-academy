def greeting():
    print('Hello World')

greeting()

# We can add properties to functions like we do with objects
greeting.lang = 'English'
print(greeting.lang)