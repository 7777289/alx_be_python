size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    # Inner loop using for to handle columns in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
