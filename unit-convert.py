# function to convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371

# function to convert miles to kilometers
def miles_to_km(miles):
    return miles * 1.60934

# function to convert fahrenheit to celsius
def f_to_c(fahrenheit):
    #subtract 32 and then multiply by 5/9 to get celsius
    return (fahrenheit - 32) * 5/9

# function to convert celsius to fahrenheit
def c_to_f(celsius):
    #multiply by 9/5 and then add 32 to get fahrenheit
    return (celsius * 9/5) + 32

# function to convert kilograms to pounds
def kg_to_lbs(kg):
    # multiply kilograms by the conversion factor to get pounds
    return kg * 2.20462

# functions to control the program workflow
def main():
    # Display the menu of conversion options to the user
    print("Unit Converter!")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Kilograms to Pounds")
    
    # the user must choose a conversion option
    choice = input("\nSelect a conversion option (1-5): ")
    
    #check if the user selected kilometers to miles
    if choice == '1':
        # get the kilometers value as a decimal (float) from the user
        km = float(input("Enter distance in kilometers: "))
        
        # call the conversion function
        miles = km_to_miles(km)
        
        # print the result with 2 decimal places
        print(f"{km} kilometers is equal to {miles:.2f} miles.")
        
        # check if the user selected miles to kilometers
    elif choice == '2':
        
        # get the miles value as a decimal (float) from the user
        miles = float(input("Enter distance in miles: "))
        
        # call the conversion function
        km = miles_to_km(miles)
        
        print(f"{miles} miles is equal to {km:.2f} kilometers.")
        
        # check if the user selected fahrenheit to celsius
    elif choice == '3':
        
        # get the fahrenheit value as a decimal (float) from the user
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        # call the conversion function
        celsius = f_to_c(fahrenheit)
        
        # print the result with 2 decimal places
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
        
        # check if the user selected celsius to fahrenheit
    elif choice == '4':
        
        # get the celsius value as a decimal (float) from the user
        celsius = float(input("Enter temperature in Celsius: "))
        
        # call the conversion function
        fahrenheit = c_to_f(celsius)
        
        # print the result with 2 decimal places
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
        
        # check if the user selected kilograms to pounds
    elif choice == '5':
        
        # get the kilograms value as a decimal (float) from the user
        kg = float(input("Enter weight in kilograms: "))
        
        # call the conversion function
        lbs = kg_to_lbs(kg)
        
        # print the result with 2 decimal places
        print(f"{kg} kilograms is equal to {lbs:.2f} pounds.")
        
        # if the user entered an invalid option, display an error message
    else:
        print("Invalid option. Please select a number between 1 and 5.")
# call the main function to start the program
if __name__ == "__main__":    main()
    