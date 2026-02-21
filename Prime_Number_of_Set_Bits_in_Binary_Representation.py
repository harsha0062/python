def countPrimeSetBits(left: int, right: int) -> int:
    # Helper function to check if a number is a small prime (2,3,5,7,11,13,17,19)
    # These are all primes <= 19 since max bit_count for 32-bit int is 32
    def isSmallPrime(x):
        return x in {2,3,5,7,11,13,17,19}
    
    ans = 0  # Counter for numbers with prime set bits
    for x in range(left, right + 1):
        # Count set bits (1s) in binary representation using bit_count()
        # If the count is a small prime, increment answer
        if isSmallPrime(x.bit_count()):
            ans += 1
    return ans  # Return total count

# Input values directly in the code
left = 6      # Start of range
right = 10    # End of range

# Call the function and print result
result = countPrimeSetBits(left, right)
print(f"Numbers from {left} to {right} with prime set bits: {result}")
