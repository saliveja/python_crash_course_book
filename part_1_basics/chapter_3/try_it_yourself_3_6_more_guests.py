
guests = ['Kerstin' , 'Elsa' , 'Erika' , 'mother' , 'Louise' , 'Marie' , 'Birgitta' , 'Sandra']
print(guests)
# Total guest list before additions

guests.insert(0, 'Karin')
print(guests)
# adding Karin at the beginning of the list

guests.insert(5, 'Linnea')
print(guests)
# adding Linnea in position number five on the list

guests.append('Canfeda')
print(guests)
# Adding Canfeda at the end of the list

# List is nor looking like this: ['Karin', 'Kerstin', 'Elsa', 'Erika', 'mother', 'Linnea', 'Louise', 'Marie', 'Birgitta', 'Sandra', 'Canfeda']


message = ", we are thirteen in total who will join the dinner on Sunday. Looking forward to see you. Bring drinks if you want annything special."
print("Hello " + guests[1] + message + "\n")
print("Hello " + guests[2] + message + "\n")
print("Hello " + guests[3] + message + "\n")
print("Hello " + guests[4] + message + "\n")
print("Hello " + guests[5] + message + "\n")
print("Hello " + guests[6] + message + "\n")
print("Hello " + guests[7] + message + "\n")
print("Hello " + guests[8] + message + "\n")
print("Hello " + guests[9] + message + "\n")
print("Hello " + guests[10] + message + "\n")
# Message to each person coming to dinner
