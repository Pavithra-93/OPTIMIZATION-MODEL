from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Create the optimization model
model = LpProblem(name="production-planning", sense=LpMaximize)

# Define decision variables
# x = units of Product A
# y = units of Product B
x = LpVariable(name="Product_A", lowBound=0, cat="Integer")
y = LpVariable(name="Product_B", lowBound=0, cat="Integer")

# Objective: Maximize profit
model += 20 * x + 30 * y, "Total_Profit"

# Constraints:
# Machine 1 usage
model += 2 * x + 1 * y <= 40, "Machine_1_Capacity"
# Machine 2 usage
model += 1 * x + 2 * y <= 60, "Machine_2_Capacity"

# Solve the model
status = model.solve()

# Show the results
print("Status:", model.status)
print(f"Optimal units of Product A: {x.value()}")
print(f"Optimal units of Product B: {y.value()}")
print("Maximum Profit:", value(model.objective))
