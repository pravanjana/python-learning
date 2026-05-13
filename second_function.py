def calculate_monthly_cost(cost_per_hour):
    return cost_per_hour * 730
cost = calculate_monthly_cost(0.096)
print(f"Monthly cost: ${cost:.2f}")

cost2 = calculate_monthly_cost(0.048)
print(f"Monthly cost: ${cost2:.2f}")

def calculate_yearly_cost(cost_per_hour):
    cost1 = calculate_monthly_cost(cost_per_hour)
    return cost1 * 12
yearly_cost = calculate_yearly_cost(0.096)
print(f"Yearly cost: $ {yearly_cost:.2f}")
