# importing classes
from car import Car, Electric_car

# from the file car, two classes are imported

my_beetle = Car('volkswagen', 'beetle', 2016)
# positional arguments for beetle
print(my_beetle.get_descriptive_name())
# calling the method in class Car

my_tesla = Electric_car('tesla', 'roadster', 2016)
# positional arguments for tesla
print(my_tesla.get_descriptive_name())
# calling the method in class Car

# importing modules
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
# when we import the whole module we need to define -->
# the name of the document as well as the class
print(my_beetle.get_descriptive_name())
# we can call the method as usual

my_tesla = car.Electric_car('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

## to import all classes from a module:
# we write --> from module_name import * <--
# not recommended bcs unclear whicih classes are being used
# errors if the import has the same name as something else in the file
