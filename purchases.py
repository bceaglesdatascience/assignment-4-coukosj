
def plus_tax(item_cost, tax):
    for item in item_cost:
        item *= tax
    return item_cost

def plus_tax(costs, tax):
    for item in range(len(costs)):
        taxed_item = costs[item] * (1+tax)
        costs[item] = taxed_item
    return costs



purchases = int(input("Number of purchases: "))
tax = float(input("Sales Tax: "))


customers = []
costs = []
totals = {}


for purchase in range(purchases):
        customer = input("Customer: ")
        customers.append(customer)
        cost = float(input("Cost: "))
        costs.append(cost)


taxed_costs = plus_tax(costs, tax)

for i in range(purchases):
    if customers[i] not in totals:
        totals[customers[i]] = costs[i]
    else:
        totals[customers[i]] = costs[i] + totals[customers[i]]

print(totals)
