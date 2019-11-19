def add_bar(items=[]):
    items.append('bar')
    return items

l = add_bar()  # l is ['bar']
l.append('foo')
print(add_bar()) # returns ['bar', 'foo', 'bar']