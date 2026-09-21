def maxNumOfSubstrings(s: str) -> list[str]:
    # Store the first and last occurrence of every character
    intervals = {}

    for i, c in enumerate(s):
        if c not in intervals:
            intervals[c] = [i, i]
        else:
            intervals[c][1] = i

    # Expand each character's interval so it includes every character
    # that appears inside the interval
    for c in intervals:
        l, r = intervals[c]

        while True:
            # Save the current interval before expanding it
            lcopy, rcopy = l, r

            # Include the complete interval of every character
            # found inside the current interval
            for i in range(lcopy, rcopy + 1):
                l = min(l, intervals[s[i]][0])
                r = max(r, intervals[s[i]][1])

            # Stop when the interval no longer changes
            if (lcopy, rcopy) == (l, r):
                break

        intervals[c] = [l, r]

    # Sort intervals by their ending positions
    candidates = sorted(intervals.values(), key=lambda x: x[1])

    # Select non-overlapping intervals greedily
    res = []
    prev = -1

    for start, end in candidates:
        if start > prev:
            res.append(s[start:end + 1])
            prev = end

    return res


# Input inside the code
s = "adefaddaccc"

print(maxNumOfSubstrings(s))