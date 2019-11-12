class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

class Bear(Animal):
    def __init__(self,name,legs=4,hibernate='yes'):
        Animal.__init__(self,name,legs)
        self.hibernate = hibernate
        
yogi = Bear('Yogi')
print(yogi.name)
print(yogi.legs)
print(yogi.hibernate)
