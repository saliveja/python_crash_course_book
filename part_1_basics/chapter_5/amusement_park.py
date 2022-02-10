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
