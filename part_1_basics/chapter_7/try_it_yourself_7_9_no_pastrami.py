sandwich_orders = ['ham sandwich', 'pastrami', 'egg sandwich',
                   'pastrami', 'pastrami', 'cheese sandwich',
                   'pastrami', 'nutella sandwich']

finished_sandwiches = []

print("\n-- An information to all customers: we are currently out of pastrami"
      " sandwiches --")
# printing info that 'pastrami' is not a part of the selection
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        # as long as 'pastrami is occuring in the list
        # 'pastrami' will be removed

    current_order = sandwich_orders.pop()
    print(f"\nI finished your {current_order.title()}.")

    finished_sandwiches.append(current_order)

finished_sandwiches.sort()
print("\nI finished these sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
