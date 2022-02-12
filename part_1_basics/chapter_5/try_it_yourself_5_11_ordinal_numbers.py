numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ~ print(numbers)
for number in numbers:
    if number == 1:
        # be careful how to write condition
        # 1 == numbers mean if 1 is in numbers
        # if 1 in numbers will print 'st' every time it finds number 1
        # and because it's a loop it will repeat even for other numbers
        print(str(number) + "st")
    elif number == 2:
        # it's also possible to write elif 2 == number:
        # watch out for if it's singular or plural reference to list
        # number or numbers
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
        # make sure else is in the for loop
