DEBUG = True

text = input("Write text: ")

binary_result = ""

for letter in text:

    ascii_value = ord(letter)
    binary = format(ascii_value, '08b')

    if DEBUG:
        print(f"DEBUG -> {letter} -> {ascii_value} -> {binary}")

    binary_result += binary + " "

print("\nBinary Output:")
print(binary_result)