def formalGreeting():
    print("How are you?")
def casualGreeting():
    print("What's up?")
def greet(type, greetFormal, greetCasual):
    if type == 'formal':
        greetFormal()
    elif type == 'casual':
        greetCasual()

# prints 'What's up?'
a = greet('casual', formalGreeting, casualGreeting)
print(a)