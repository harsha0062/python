# Function to add two binary strings and return the result as a binary string
# Converts binary strings to integers, adds them, and converts back to binary
def addBinary(a: str, b: str) -> str:
    l = int(a, 2)      # Convert binary string a to integer (base 2)
    l1 = int(b, 2)     # Convert binary string b to integer (base 2)
    l2 = l + l1        # Add the two integers
    return bin(l2)[2:] # Convert sum back to binary and remove '0b' prefix

# Input binary strings (hardcoded as requested)
a = "1010"  # Binary number 10 in decimal
b = "11"    # Binary number 3 in decimal

# Call the function and print result
result = addBinary(a, b)
print(f"Binary a: {a} ({int(a,2)}) + Binary b: {b} ({int(b,2)}) = {result} ({int(result,2)})") 
# Output: Binary a: 1010 (10) + Binary b: 11 (3) = 1101 (13)
