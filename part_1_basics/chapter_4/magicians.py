
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# the names are printed one after one, each on a new line
    

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
# if we don't define the list again, the name will be sorted alphabetcially
    
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# we can write as many lines as we wish in the for loop
    
print("Thank you, everyone. That was a great magic show!")
# this print concludes the loop (not a part of indent
# It will be printed only once
# indentation is used to show that one line is connected to another
# indentation also help with organizing code

for magician in magicians:
print(magician)
# python will communicate - indentation error 
# if there is no indent when using for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
# Geany reports indentation errors, & won't print the line explained in book
# The last print will refer to last known information
# It will lokk like this:

# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina

message = "Hello Python world!"
    print(message)
    # python communicates that it's an unexpected indent
    
magicians = ['alice', 'david', 'carolina']
for magicians in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you everyone, that was a great magic show!")
# bcs the last line is indented, it will be printed for each magician

