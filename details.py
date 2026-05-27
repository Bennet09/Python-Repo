# Get the user's first name
import re


first_name = input("Enter your first name: ")

# Get the user's surname
surname = input("Enter your surname: ")

# Get the user's birth year
birth_year = int(input("Enter your birth year: "))

# Current year
current_year = 2026

# Calculate age
age = current_year - birth_year

# Display greeting message
print(f"\nHi {first_name} {surname}")
print(f"You are {age} years old this year")

# Combine name and surname
full_name = first_name + " " + surname

# Use regex to find all vowels in the full name
vowels = re.findall(r"[aeiouAEIOU]", full_name)

# Display vowels found
print("\nVowels found in your name and surname:")
print(vowels)