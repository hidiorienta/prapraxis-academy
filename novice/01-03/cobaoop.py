class ZooMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Zoo Member)'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Mother(ZooMember):
    def __init__(self, name, age, food):
        ZooMember.__init__(self, name, age)
        self.food = food
        print('(Mother name: {})'.format(self.name))
    
    def tell(self):
        ZooMember.tell(self)
        print('Food: "{}"'.format(self.food))

class Cub(ZooMember):
    def __init__(self, name, age, species):
        ZooMember.__init__(self, name, age)
        self.species = species
        print('(Cub name: {})'.format(self.name))

    def tell(self):
        ZooMember.tell(self)
        print('Species: "{}"'.format(self.species))

m1 = Mother('Luna', 30, 'Meat')
m2 = Mother('Lina', 25, 'Grass')
c1 = Cub('Ron', 2, 'Lion')
c2 = Cub('Duf', 1, 'Deer')

print()

members = [m1, m2, c1, c2]
for member in members:
    member.tell()