## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a type of animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name attribute
        self.name = name

## Cat is-a type of animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name attribute
        self.name = name

## Person is-a class at top level inheriting from object
class Person(object):

    def __init__(self, name):
        ## Person in instatiated with a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a type of person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is a class
class Fish(object):
    pass

## Salmon is-a type of Fish
class Salmon(Fish):
    pass

## Halibut is-a type of Fish
class Halibut(Fish):
    pass


## rover is-a Dog object
rover = Dog("Rover")
print "Rover's name is ", rover.name

## satan is-a Cat object
satan = Cat("Satan")
print "Satan's name is ", satan.name

## Mary is-a Person object
mary = Person("Mary")
print "Mary's name is ", mary.name

## Mary's has-a pet, which is a cat Object
mary.pet = satan
print "Mary's pet's name is ", mary.pet.name

## Frank is-an employee with salary of 120000
frank = Employee("Frank", 120000)
print "Frank's name is ", frank.name
print "Frank earns ", frank.salary

## Frank has-a pet, rover, which is a Dog
frank.pet = rover
print "Frank's pet's name is ", frank.pet.name

## flipper is-a fish object
flipper = Fish()

## crouse is a salmon object
crouse = Salmon()

## harry is-a Halibut object
harry = Halibut()
