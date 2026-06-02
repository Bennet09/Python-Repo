# Binary to character 

## Overview

The purpose of this script is to convert text entered by the user into its binary representation.

Computers store characters as numbers using the ASCII standard. These numbers can then be converted into binary, which is the language computers use internally.

For example:

Letter:

A

ASCII Value:

65

Binary Value:

01000001

The script performs this conversion for every character entered by the user.

---

## Step 1: Getting User Input

```python
text = input("Enter text: ")
```

### What this command does

The `input()` function waits for the user to type something.

Example:

```text
Enter text: CAT
```

The entered text is stored inside the variable called `text`.

After the user enters CAT:

```python
text = "CAT"
```

---

## Step 2: Creating an Empty Variable

```python
binary_result = ""
```

### What this command does

This creates an empty string.

The purpose of this variable is to store all binary values generated during the conversion process.

Initially:

```python
binary_result = ""
```

contains nothing.

---

## Step 3: Looping Through Each Character

```python
for letter in text:
```

### What this command does

The `for` loop processes one character at a time.

If the user enters:

```python
text = "CAT"
```

the loop runs three times:

Iteration 1:

```python
letter = "C"
```

Iteration 2:

```python
letter = "A"
```

Iteration 3:

```python
letter = "T"
```

This allows the program to convert every character individually.

---

## Step 4: Converting a Character to ASCII

```python
ascii_value = ord(letter)
```

### What this command does

The `ord()` function converts a character into its ASCII numerical value.

Examples:

```python
ord("A")
```

returns:

```text
65
```

```python
ord("C")
```

returns:

```text
67
```

The result is stored inside the variable `ascii_value`.

Example:

```python
ascii_value = 67
```

---

## Step 5: Converting ASCII to Binary

```python
binary = format(ascii_value, '08b')
```

### What this command does

The `format()` function converts a number into binary format.

Example:

```python
format(67, '08b')
```

returns:

```text
01000011
```

### Understanding '08b'

The format specification consists of:

| Symbol | Meaning                             |
| ------ | ----------------------------------- |
| 0      | Fill empty positions with zeros     |
| 8      | Ensure the result contains 8 digits |
| b      | Convert to binary                   |

Example:

```python
format(5, '08b')
```

Output:

```text
00000101
```

Without `'08b'`, the binary value would simply be:

```text
101
```

The leading zeros ensure a consistent 8-bit binary format.

---

## Step 6: Displaying Debug Information

```python
print(f"DEBUG -> {letter}: {ascii_value} -> {binary}")
```

### What this command does

This statement displays the current conversion process.

Example output:

```text
DEBUG -> C: 67 -> 01000011
```

This shows:

1. The original character
2. Its ASCII value
3. Its binary value

Debug statements are useful for verifying that the program is working correctly.

---

## Step 7: Building the Final Binary String

```python
binary_result += binary + " "
```

### What this command does

This adds the newly generated binary value to the growing result string.

The `+=` operator means:

```python
binary_result = binary_result + binary + " "
```

Example:

Before:

```python
binary_result = ""
```

After processing C:

```python
binary_result = "01000011 "
```

After processing A:

```python
binary_result = "01000011 01000001 "
```

After processing T:

```python
binary_result = "01000011 01000001 01010100 "
```

Each binary value is added to the end of the string.

---

## Step 8: Displaying the Final Result

```python
print("\nBinary Output:")
print(binary_result)
```

### What this command does

The first statement displays a heading.

The `\n` creates a new line before the heading.

Output:

```text
Binary Output:
```

The second statement displays the complete binary conversion.

Example:

```text
01000011 01000001 01010100
```

---

## How the Commands Work Together

The complete conversion process follows these steps:

1. User enters text.
2. The program examines one character at a time.
3. Each character is converted into its ASCII value using `ord()`.
4. The ASCII value is converted into binary using `format()`.
5. Debug information is displayed.
6. The binary value is added to the result string.
7. The process repeats until all characters have been processed.
8. The final binary string is displayed.

Example:

```text
Input:
CAT

Conversion Process:

C -> 67 -> 01000011
A -> 65 -> 01000001
T -> 84 -> 01010100

Final Output:

01000011 01000001 01010100
```

This demonstrates how text can be translated into the binary format used by computers.
