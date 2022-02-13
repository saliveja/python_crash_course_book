rivers = {'Mesopotamia': 'Eufrates',
          'Russia': 'Ural river',
          'Czech republic': 'Vltava'
          }
# using loop to print a sentence about each value
for key in rivers:
    if key == 'Mesopotamia':
        print("Eufrates runs through Mesopotamia, in the land between rivers.")
    if key == 'Russia':
        print("The Ural river flows through Russia and Kazakhstan.")
    if key == 'Czech republic':
        print("Vltava is the longest river in Czech Republic.")
print("\n")

# printing the name of each river
for river in rivers.values():
    print(river.title())
print("\n")

for key in rivers.keys():
    print(key.title())
