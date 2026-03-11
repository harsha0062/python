def bitwiseComplement(n: int) -> int:
    """
    Return bitwise complement of n (flip all bits in its binary representation).
    Creates mask with same bit length as n, then XORs with n to flip bits.
    """
    if n == 0:
        return 1  # Special case: complement of 0 is 1
    
    mask = 1              # Start with 1 (binary: 1)
    while mask < n:       # Build mask until it covers all bits of n
        mask = (mask << 1) | 1  # Left shift + set LSB: 1→11→111→1111...
    
    return n ^ mask       # XOR flips all bits where mask has 1s


# Test cases with inputs inside code
print("n=5 ->", bitwiseComplement(5))      # 5=101 → 010 = 2 ✓
print("n=7 ->", bitwiseComplement(7))      # 7=111 → 000 = 0 ✓
print("n=0 ->", bitwiseComplement(0))      # 0     → 1   ✓
print("n=10 ->", bitwiseComplement(10))    # 10=1010→0101=5 ✓

# Visualize the mask building:
print("\nMask building for n=10 (1010):")
n = 10
mask = 1
print(f"n=10 (binary: {bin(n)[2:].zfill(4)})")
while mask < n:
    print(f"mask={mask:>2} ({bin(mask)[2:].zfill(4)}) -> shift|1 = {bin((mask<<1)|1)[2:].zfill(4)}")
    mask = (mask << 1) | 1
print(f"Final mask={mask} ({bin(mask)[2:].zfill(4)}) ^ n = {n ^ mask}")
