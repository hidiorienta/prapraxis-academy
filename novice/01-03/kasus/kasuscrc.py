class Gadget:
    def __init__(self, gadgetlist, price):
        self.gadgetlist = gadgetlist
        self.price = price
        print('(Gadget: {})'.format(self.gadgetlist))

    def tell(self):
        print('Gadget List:"{}", Price:"{}"'.format(self.gadgetlist, self.age), end=" ")

class Brand(Gadget):
    def __init__(self, brandlist, type, price, releaseyear, g1):
        Gadget.__init__(self, brandlist, type, price, releaseyear, g1)
        self.brandlist = brandlist
        self.type = type
        self.releaseyear = releaseyear
        self.gadget = g1
        print('(Brand: {})'.format(self.gadgetlist))
    
    def tell(self):
        Gadget.tell(self)
        print('Brand: "{}", Type: "{}", Release Year: "{}"'.format(self.brandlist, self.type, self.releaseyear))

class Specification(Gadget):
    def __init__(self, processor, memory, storage):
        Gadget.__init__(self, gadgetlist, price)
        self.processor = processor
        self.memory = memory
        self.storage = storage
        print('(Specification: {})'.format(self.gadgetlist))
    
    def tell(self):
        Gadget.tell(self)
        print('Processor: "{}", Memory: "{}", Storage: "{}"'.format(self.processor, self.memory, self.storage))

g1 = Gadget('Laptop', 50000000)
g2 = Gadget('Handphone', 10000000)
b1 = Brand('Asus', 'ROG', 50000000, 2019, g1)
b2 = Brand('Samsung', 'S10', 10000000, 2018, g2)
s1 = Specification('Intel Core i7', '16GB', '1TB', b1)
s2 = Specification('Exynos', '8GB', '512GB', b2)

print()

members = [g1, g2, b1, b2, s1, s2]
for member in members:
    member.tell()