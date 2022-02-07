# list with values print differently
cars = ['audio', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# if the car is a bmw it will be printed with upper case letters
# if it's any other car, it will be printed with first letter upper case
# if --> is a conditional test

car = 'bmw'
car == 'bmw'
# first car equals bmw
# second conditional test on if it's a bmw
# respons is True
