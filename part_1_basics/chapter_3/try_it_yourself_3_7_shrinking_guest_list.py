guests = ['Karin', 'Kerstin', 'Elsa', 'Erika', 'mother', 'Linnea', 'Louise', \
          'Marie', 'Birgitta', 'Sandra', 'Canfeda']
print(guests)
# complete guest list before changes

message = ", due to unforseen changes I'm unable to invite more than two \
people for dinner. I appologize for this inconvenience, I'll update with more \
information soon."
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
# printing message that only two people can come

guest_not_coming_1 = guests.pop(0)
print(guests)
# removing a person from the list with variable guest_not_coming_1

print(guest_not_coming_1.title() + ", I'm sorry, I'm not able to invite you \
for dinner this Sunday. Hope we can meet soon. Take care.")
print(guests)
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
print(guests.pop(0).title() + ", I'm sorry, I'm not able to invite you for \
dinner this Sunday. Hope we can meet soon. Take care.")
# changing removal system to include pop methods in the print command 
# adding a message explaining that I can't invite them

guest_1 = "Sandra"
guest_2 = "Canfeda"
message = ", I'm sorry for all the mess with the invitations. It would be \
amazing if you still would like to come to the dinner on Sunday. Looking \
forward to see you!\n"
print("Dear " + guest_1.title() + ", " + message)
print("Dear " + guest_2.title() + ", " + message)
# inviting the two remaining people on the guest list

guests = ['Sandra', 'Canfeda']
del guests[0]
del guests[0]
print(guests)
# deleting the last two names on the list. When printing receiving []
# exercise finished
