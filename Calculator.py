from classes.ComplexNumber import operations

# Introduction to the program
print("Complex Number Calculator")
print("==========================")
print("This program performs operations on complex numbers.")
print("Enter two complex numbers (a+bi).")

# Example usage:
print("Example: 34")

# Take input from the user
while True:

    input_values = input("Enter z1: ")
    a1, b1 = float(input_values[0]), float(input_values[1])
    z1 = operations(a1, b1)

    input_values = input("Enter z2: ")
    a2, b2 = float(input_values[0]), float(input_values[1])
    z2 = operations(a2, b2)

    # Print complex numbers before operations
    print("z1:", z1)
    print("z2:", z2)
    
    respuesta = input("Do you want to continue with these numbers? (yes/no):")

    if respuesta.lower() == "no": 
        print("\nPlease enter the numbers again")
        
    if respuesta.lower() == "yes":
        # Perform operations on complex numbers
        # Addition operations
        print("\nAddition:", z1 + z2)

        # Subtraction operations
        print("Subtraction:", z1 - z2)

        # Multiplication operations
        print("Multiplication:", z1 * z2)
        
        # Division operations
        try:
            print("Division:", z1 / z2)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

        # GoodBye messagge
        print("\nGoodbye!")
        break
    