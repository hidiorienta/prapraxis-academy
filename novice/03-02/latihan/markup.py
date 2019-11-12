from flask import Markup
print(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')

print(Markup.escape('<blink>hacker</blink>'))

print(Markup('<em>Marked up</em> &raquo; HTML').striptags())