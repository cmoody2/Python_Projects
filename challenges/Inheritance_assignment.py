

class Bag:
    def __init__(self,name,manufacturer,num_of_compartments):
        self.name = name
        self.manufacturer = manufacturer
        self.num_of_compartments = num_of_compartments

class Backpack(Bag):
    waterproof = 'Yes'
    num_of_straps = 2

class LaptopBag(Bag):
    max_laptop_size = 15.6
    num_of_straps = 1

B1 = LaptopBag("Classic Slim","Targus",3)

print("New Store Arrival!\n\n{} '{}' \nCompartments: {} \nLaptop Size Compatibility: {} \nNumber of Straps: {}\
".format(B1.manufacturer,B1.name,B1.num_of_compartments,B1.max_laptop_size,B1.num_of_straps))
