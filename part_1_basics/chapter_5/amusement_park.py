# admissions for anyone under age 4 is free.
# admission for anyone between the ages of 4 and 18 is $5.
# admission for anyone age 18 or older is $10.

# if-elif-else
age = 12
if age < 4:
    print("Your admission cost is $0.")
    # tests if the person is 4 years old
elif age < 18:
    print("your admission cost is $5.")
    # is another conditional test that will only run if the previous fails
    # because the first test was False, this run and proves True
    # the text is printed
else:
    print("Your admission cost is $10.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")
# this code is more efficient and easier to modify

# using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# this adds and extra condition. if the person is less than 65 years it cost 10
# but if not then it cost 5, so everyone older than 65 will pay 5

# we can also do the code without else: at the end
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")
# the last elif mean that if a person is more than or equal to 65 then \
# the cost is 5
