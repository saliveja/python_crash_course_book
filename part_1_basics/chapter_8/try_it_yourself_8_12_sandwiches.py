def sandwich(*toppings):
    print("You ordered these sandwiches:")
    for topping in toppings:
        print(f"- {topping}")


sandwich('cheese')
print("\n")
sandwich('hoummus', 'cucumber')
print("\n")
sandwich('butter', 'vegiar', 'cheese', 'sallad')
