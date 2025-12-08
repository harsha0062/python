import math  # Import math module for square root function

# Function to count the number of square sum triples
# A square triple (a, b, c) satisfies: a^2 + b^2 = c^2 and 1 <= a, b, c <= n
def countTriples(n: int) -> int:
    count = 0
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Iterate b from a+1 to n to avoid duplicate unordered pairs (a, b)
        for b in range(a + 1, n + 1):
            # Compute a^2 + b^2
            x = a * a + b * b
            # Take integer square root of x
            c = int(math.sqrt(x))
            # Check if c is an integer square root and within range 1..n
            # If valid, there are 2 ordered triples: (a, b, c) and (b, a, c)
            if (c * c == x) and c <= n:
                count += 2
    return count

# ---------------- Input and output section ----------------

# You can change this value to test with different inputs
n = 5  # Example input; for LeetCode 1925, n can be up to 250

# Call the function and print the result
result = countTriples(n)
print(result)
