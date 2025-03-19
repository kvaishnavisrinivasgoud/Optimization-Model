# Optimization-Model
## Solving a Business Problem Using Optimization Techniques (Linear Programming) and Python Libraries like Pulp
In this notebook, we will solve a business problem using Linear Programming (LP) and the Pulp library in Python. The problem we will address is a classic production optimization problem, where a company wants to maximize its profit by determining the optimal number of units to produce for each product, given constraints like resource availability and demand.

## Problem Statement
A company manufactures two products: Product A and Product B. The production of these products requires two resources: Resource 1 and Resource 2. The company wants to maximize its profit while adhering to the following constraints:

1.Resource Constraints:

-Each unit of Product A requires 2 units of Resource 1 and 1 unit of Resource 2.

-Each unit of Product B requires 1 unit of Resource 1 and 3 units of Resource 2.

-The company has a total of 100 units of Resource 1 and 90 units of Resource 2 available.

2.Demand Constraints:

-The maximum demand for Product A is 40 units.

-The maximum demand for Product B is 30 units.

3.Profit:

-The profit per unit of Product A is $50.

-The profit per unit of Product B is $70.

Our goal is to determine the optimal number of units to produce for Product A and Product B to maximize the company's profit.


## Step 1: Install and Import Required Libraries
We will use the PuLP library to model and solve this linear programming problem. If you don't have PuLP installed, you can install it using:

                                              !pip install pulp


Now, let's import the required libraries:

                                               import pulp


## Step 2: Define the Problem
We will define the problem as a maximization problem since the goal is to maximize profit.


## Step 3: Define Decision Variables
We need to define decision variables for the number of units to produce for Product A and Product B. These variables must be non-negative.


## Step 4: Define the Objective Function
The objective is to maximize the total profit, which is calculated as:

Profit=50×Product A+70×Product B


## Step 5: Define Constraints
We will add the resource and demand constraints to the problem.

1.Resource Constraints:

  2×Product A+1×Product B≤100(Resource 1)

  1×Product A+3×Product B≤90(Resource 2)

2.Demand Constraints:

   Product A≤40

   Product B≤30


## Step 6: Solve the Problem
Now, we will solve the problem using the default solver in Pulp.


## Step 7: Analyze the Results
Let's check the status of the solution and the optimal values for Product A and Product B.


## Step 8: Interpret the Results
The output will provide the optimal number of units to produce for Product A and Product B and the maximum profit achievable under the given constraints.



## Insights
The optimal production plan is to produce 30 units of Product A and 20 units of Product B.

This plan maximizes the profit to $2900 while respecting the resource and demand constraints.

The solution is optimal, meaning no oother combination of production quantities will yield a higher profit under the given constraints.


## Conclusion
This notebook demonstrates how to use Linear Programming and the PuLP library in Python to solve a business optimization problem. By defining decision variables, an objective function, and constraints, we can efficiently determine the optimal solution to maximize profit or minimize costs in various business scenarios.


## Next Steps
1.Experiment with different constraints (e.g., changing resource availability or demand limits).

2.Extend the model to include more products or resources.

3.Explore other optimization techniques (e.g., integer programming, nonlinear programming) for more complex problems.


## Output

[Expected Output.txt](https://github.com/user-attachments/files/19342900/Expected.Output.txt)

