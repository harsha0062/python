from collections import defaultdict

def maxNumberOfBalloons(text: str) -> int:
    """
    Return the maximum number of times the word "balloon" can be formed
    from the letters in `text`.
    Note: "balloon" requires:
      b:1, a:1, l:2, o:2, n:1
    """
    fm = defaultdict(int)

    for c in text:
        # Only count letters that appear in "balloon"
        if c in "balon":   # 'l' and 'o' will be counted twice in requirement below
            fm[c] += 1

    # For 'l' and 'o' we need two occurrences per "balloon"
    return min(fm['b'], fm['a'], fm['l'] // 2, fm['o'] // 2, fm['n'])


# Test cases inside the file (no if __name__ guard)
texts = [
    "nlaebolko",            # expected 1 ("balloon")
    "loonbalxballpoon",     # expected 2
    "leetcode",             # expected 0
    "balloonballoonballoo", # expected 2 (insufficient 'o' for 3)
    "",                     # expected 0
]

for t in texts:
    print(f"text = {t!r}, maxNumberOfBalloons = {maxNumberOfBalloons(t)}")