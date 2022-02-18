sandwich_orders = ['ham sandwich', 'egg sandwich', 'cheese sandwich',
                   'nutella sandwich']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\nI finished your {current_order.title()}.")

    finished_sandwiches.append(current_order)

finished_sandwiches.sort()
print("\nI finished these sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())