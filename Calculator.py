from classes.ComplexNumber import operations

# Introduction to the program
print("Complex Number Calculator")
print("==========================")
print("This program performs operations on complex numbers.")
print("Enter two complex numbers (a+bi) separated in a single line.")

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
    print(f"z1: {z1}")
    print(f"z2: {z2}")
    
    respuesta = input("\nDo you want to continue with these numbers? (yes/no):")

    if respuesta.lower() == "no": 
        print("\nPlease enter the numbers again")
        continue  
    
    # Perform operations on complex numbers   
    elif respuesta.lower() == "yes":
        while True:
            # Show the options for the user to select
            option = input(
                "\nPlease enter the option:\n"
                "1. Addition\n"
                "2. Subtraction\n"
                "3. Multiplication\n"
                "4. Division\n"
                "5. Exit\n"
            )

            # Perform the operation based on the user's choice
            if option == "1":
                print("\nAddition:", z1 + z2)
                
            elif option == "2":
                print("Subtraction:", z1 - z2)
                
            elif option == "3":
                print("Multiplication:", z1 * z2)
                
            elif option == "4":
                try:
                    print("Division:", z1 / z2)
                except ZeroDivisionError as e:
                    print(e)
                    
            elif option == "5":
                print("\nGoodbye!")
                exit()
            else:
                print("Invalid option. Please try again.")
                continue
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")