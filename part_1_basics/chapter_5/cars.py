# list with values print differently
cars = ['audio', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    # if the car is a bmw it will be printed with upper case letters
    else:
        print(car.title())
# if it's any other car, it will be printed with first letter upper case
# if --> is a conditional test

car = 'bmw'
car == 'bmw'
# first car equals bmw
# second conditional test on if it's a bmw
# respons is: True

car = 'Audi'
car.lower() == 'audi'
# response: True
# will make all letters in the statement lower case before testing equality
# if car is printed it will show 'Audi'
