number = input("How many people are you in your dinner group? ")
number = int(number)
if number > 8:
    # if the number is higher than 8
    print(f"\nI'm sorry but at the moment we don't have any table "
          f"for this many people. You will have to wait for a moment.")
else:
    print("Your table is ready, welcome!")
