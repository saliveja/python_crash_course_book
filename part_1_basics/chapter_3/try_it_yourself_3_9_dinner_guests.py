
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


message = str(len(guests)) + " people will come to the dinner."
print(message)
