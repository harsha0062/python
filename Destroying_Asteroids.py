from typing import List

def asteroidsDestroyed(mass: int, asteroids: List[int]) -> bool:
    """
    Determine whether all asteroids can be destroyed given initial mass.

    Rules:
        - You can collide with asteroids in any order.
        - If your mass >= asteroid's mass, you destroy it and absorb its mass.
        - If your mass < asteroid's mass, you are destroyed.

    Strategy:
        - Sort asteroids in non-decreasing order.
        - Always try to destroy the smallest asteroid you haven't yet.
        - If at any point your mass is less than the current asteroid, return False.
        - Otherwise, keep adding asteroid masses to your mass.
        - If you destroy all asteroids, return True.

    This greedy approach works because destroying a smaller asteroid first
    only increases your mass, making it easier to destroy larger ones later.
    """
    asteroids.sort()  # Sort asteroids from smallest to largest

    for a in asteroids:
        if a > mass:
            # Cannot destroy this asteroid
            return False
        mass += a  # Absorb its mass

    return True


# Test cases with inputs written directly in code (no `if __name__ == "__main__"`)
mass1 = 10
asteroids1 = [3, 9, 19, 5, 21]
print("mass =", mass1)
print("asteroids =", asteroids1)
print("asteroidsDestroyed =", asteroidsDestroyed(mass1, asteroids1.copy()))
# Sorted: [3, 5, 9, 19, 21]
# 10 >= 3 → mass=13
# 13 >= 5 → mass=18
# 18 >= 9 → mass=27
# 27 >= 19 → mass=46
# 46 >= 21 → mass=67 → True

mass2 = 5
asteroids2 = [4, 9, 23, 4]
print("\nmass =", mass2)
print("asteroids =", asteroids2)
print("asteroidsDestroyed =", asteroidsDestroyed(mass2, asteroids2.copy()))
# Sorted: [4, 4, 9, 23]
# 5 >= 4 → mass=9
# 9 >= 4 → mass=13
# 13 >= 9 → mass=22
# 22 < 23 → False

mass3 = 100
asteroids3 = [10, 20, 30, 40]
print("\nmass =", mass3)
print("asteroids =", asteroids3)
print("asteroidsDestroyed =", asteroidsDestroyed(mass3, asteroids3.copy()))
# Should be True

# Trace for first example
print("\nTrace for mass=10, asteroids=[3,9,19,5,21]:")
mass = 10
asteroids = [3, 9, 19, 5, 21]
asteroids.sort()
print("Sorted asteroids:", asteroids)
for a in asteroids:
    print(f"  current mass={mass}, asteroid={a} → ", end="")
    if a > mass:
        print("cannot destroy → False")
        break
    mass += a
    print(f"destroy, new mass={mass}")
else:
    print("All destroyed → True")