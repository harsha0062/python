from typing import List


# Your function
def totalNumbers(digits: List[int]) -> int:
    n=len(digits)
    res=set()

    # Choose the hundreds digit
    for i in range(n):

        # Choose the tens digit
        for j in range(n):

            # Choose the units digit
            for k in range(n):

                # Skip if:
                # 1. Any two positions are the same
                # 2. Hundreds digit is 0
                # 3. Units digit is odd
                if i in (j,k) or j in (i,k) or digits[i]==0 or digits[k]%2==1:
                    continue

                # Form the 3-digit number
                num=(digits[i]*100)+(digits[j]*10)+digits[k]

                # Set automatically removes duplicate numbers
                res.add(num)

    # Return number of unique 3-digit numbers
    return len(res)


# ----------------------------------------
# INPUT
# ----------------------------------------

digits = [1, 2, 3, 4]


# Call the function
answer = totalNumbers(digits)


# Print the answer
print("Total number of unique 3-digit numbers:", answer)