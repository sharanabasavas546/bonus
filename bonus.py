import sys

# Check if the correct number of arguments is provided
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    salary = 50000.0
    print("No input given - using default value:")

# Calculate bonus
bonus = 0.10 * salary
total_salary = salary + bonus

# Display results
print(f"Script Name: {script_name}")
print(f"Salary: ₹{salary:.2f}")
print(f"Bonus amount: ₹{bonus:.2f}")
print(f"Total salary after adding bonus: ₹{total_salary:.2f}")
