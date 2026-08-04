def maxRepeating(sequence: str, word: str) -> int:
    # Start checking from zero repetitions
    count = 0

    while True:
        # If word repeated count times is not found in sequence,
        # the previous count was the maximum valid repetition count
        if word * count not in sequence:
            return count - 1

        # Check the next repetition count
        count += 1


# Input inside the code
sequence = "ababc"
word = "ab"

print(maxRepeating(sequence, word))