import pulp
# Initialize the problem
problem = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)
# Define decision variables
product_A = pulp.LpVariable("Product_A", lowBound=0, cat="Integer")  # Units of Product A
product_B = pulp.LpVariable("Product_B", lowBound=0, cat="Integer")  # Units of Product B
# Define the objective function
problem += 50 * product_A + 70 * product_B, "Total_Profit"
# Add resource constraints
problem += 2 * product_A + 1 * product_B <= 100, "Resource_1"
problem += 1 * product_A + 3 * product_B <= 90, "Resource_2"

# Add demand constraints
problem += product_A <= 40, "Demand_A"
problem += product_B <= 30, "Demand_B"
# Solve the problem
problem.solve()
# Check the status of the solution
status = pulp.LpStatus[problem.status]
print(f"Status: {status}")

# Print the optimal values
print(f"Units of Product A to produce: {pulp.value(product_A)}")
print(f"Units of Product B to produce: {pulp.value(product_B)}")
print(f"Total Profit: ${pulp.value(problem.objective)}")
