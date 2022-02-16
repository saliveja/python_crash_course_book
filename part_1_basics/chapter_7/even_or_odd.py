number = input("Enter a number, and I'll tell your if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    # even numbers can be divided by two
    # when writing 6 % 3 it returns zero because nothing remains
    # while if I write 5 % 3 it will return 2
    # so this means that if this condition is met, the number is even
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
