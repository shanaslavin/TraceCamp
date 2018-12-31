# Parent class
class Dog:

    # Class attribute
    species = 'assholes'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.walking = False

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    # modify
    def eat(self):
        self.is_hungry = False 
    
    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Pets Class
class Pets:
    
    def __init__(self, dogs):
        self.animals = dogs
    
    def print_animals(self):
        for animal in self.animals:
            print("{} is {}".format(animal.name, animal.age))
        
        print("And they're all {}, of course".format(Dog.species))
    
    def feed_animals(self):
        for self.animals in self.dogs:
            if(self.animals.is_hungry):
                self.animals.eat()

    def hungry(self):
        for animal in self.animals:
            if(animal.is_hungry):
                print("{} is hungry".format(animal.name))
            else:
                print("{} is not hungry".format(animal.name))
    
    def feed(self):
        for animal in self.animals:
            animal.eat()
    
    def walk(self):
        for animal in self.animals:
            print("{} is walking!".format(animal.name))

# Output
animals = [ Dog("Apricot", 7), Dog("Hemmingway", 1), Dog("Nala", 1)]
my_animals = Pets(animals)
print("I have ", len(animals), " animals")
my_animals.print_animals()
my_animals.hungry()
my_animals.feed()
print("Feeding the aninals")
my_animals.hungry()
my_animals.walk()

