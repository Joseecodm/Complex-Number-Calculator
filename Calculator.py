from classes.ComplexNumber import operations

# Introduction to the program
print("Complex Number Calculator")
print("==========================")
print("This program performs operations on complex numbers.")
print("Enter two complex numbers (a+bi) separated by space.")

# Example usage:
print("Example: 3 4")

# Take input from the user
input_values = input("Enter z1 ")
a1, b1 = int(input_values[0]), int(input_values[1])
z1 = operations(a1, b1)

input_values = input("Enter z2")
a2, b2 = int(input_values[0]), int(input_values[1])
z2 = operations(a2, b2)

# Print complex numbers before operations
print("z1:", z1)
print("z2:", z2)

# Addition operations
print("Addition:", z1 + z2)

# Subtraction operations
print("Subtraction:", z1 - z2)