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
print(my_beetle.get_descriptive_name())

my_tesla = car.Electric_car('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
