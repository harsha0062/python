from typing import List
from math import inf

# ----------------------------------------------------------------
# TrieNode: each node stores:
#   - children: dict mapping char -> TrieNode
#   - smallest: minimum length of any word that passes through this node
#   - idx: index of the word with that smallest length (among those passing through)
# ----------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.smallest = inf
        self.idx = inf


# ----------------------------------------------------------------
# Trie for storing reversed words from wordsContainer.
# Each path corresponds to a reversed word's prefix (i.e., a suffix of the original word).
# At each node, we track the index of the word with the smallest length
# among all words that share the prefix up to this node.
# ----------------------------------------------------------------
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str, idx: int) -> None:
        """
        Insert reversed word `s` into the trie, with its original index `idx`.
        At each node along the path, update:
            - smallest = min(smallest, len(s))
            - idx = original index of the word with that smallest length
        """
        curr = self.root

        # Update root
        if len(s) < curr.smallest:
            curr.smallest = len(s)
            curr.idx = idx

        for c in s:
            # Create child node if it doesn't exist
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

            # Update this node with the smaller length / index
            if len(s) < curr.smallest:
                curr.smallest = len(s)
                curr.idx = idx

    def query(self, s: str) -> int:
        """
        Query the trie with reversed query word `s`.
        Traverse as far as possible following characters in `s`.
        Return the index stored at the last node reached.
        If some prefix is missing, return the index from the last existing node.
        """
        curr = self.root

        for c in s:
            if c not in curr.children:
                break
            curr = curr.children[c]

        # Return the index of the word with the smallest length
        # that shares this prefix with the query.
        return curr.idx


# ----------------------------------------------------------------
# Main function: for each query word, find the index of the word in
# wordsContainer that has the longest common suffix with the query,
# and among those, the one with the smallest length.
# We achieve this by storing reversed words and querying their prefixes.
# ----------------------------------------------------------------
def stringIndices(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    """
    Given:
      - wordsContainer: list of words
      - wordsQuery: list of query words

    For each query word q, find the index i such that:
      - wordsContainer[i] and q share the longest common suffix, and
      - among those, wordsContainer[i] has the smallest length (breaking ties by smaller index implicitly).

    We:
      - Reverse all words before inserting/querying.
      - Use a trie of reversed words.
      - At each trie node, store the index of the word with the smallest length.
      - For each query, traverse the trie as far as possible and return the stored index.
    """
    trie = Trie()
    res = []

    # Insert all words from container (reversed) into the trie
    for i, w in enumerate(wordsContainer):
        trie.insert(w[::-1], i)

    # For each query word, query the trie (reversed)
    for w in wordsQuery:
        res.append(trie.query(w[::-1]))

    return res


# ----------------------------------------------------------------
# Test cases with inputs inside code (no `if __name__ == "__main__"`)
# ----------------------------------------------------------------
wordsContainer1 = ["a", "b", "ba"]
wordsQuery1 = ["a", "ba", "b"]

print("wordsContainer =", wordsContainer1)
print("wordsQuery =", wordsQuery1)
print("stringIndices =", stringIndices(wordsContainer1, wordsQuery1))

wordsContainer2 = ["abc", "bc", "a", "b"]
wordsQuery2 = ["c", "cc", "abc"]

print("\nwordsContainer =", wordsContainer2)
print("wordsQuery =", wordsQuery2)
print("stringIndices =", stringIndices(wordsContainer2, wordsQuery2))

wordsContainer3 = ["abcd", "bcd", "cd", "d"]
wordsQuery3 = ["d", "cd", "bcd", "abcd"]

print("\nwordsContainer =", wordsContainer3)
print("wordsQuery =", wordsQuery3)
print("stringIndices =", stringIndices(wordsContainer3, wordsQuery3))