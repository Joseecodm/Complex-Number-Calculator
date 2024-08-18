from classes.ComplexNumber import operations

# Introduction to the program
print("Complex Number Calculator")
print("==========================")
print("This program performs operations on complex numbers.")
print("Enter two complex numbers (a+bi) separated by space.")

# Example usage:
print("\n")

# Take input from the user
while True:

    real_z1 = input("Enter real part of z1: ")
    imaginary_z1 = input("Enter imaginary part of z1: ")
    a1, b1 = float(real_z1), float(imaginary_z1)
    z1 = operations(a1, b1)

    real_z2 = input("\nEnter real part of z2: ")
    imaginary_z2 = input("Enter imaginary part of z2: ")
    a2, b2 = float(real_z2), float(imaginary_z2)
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
    