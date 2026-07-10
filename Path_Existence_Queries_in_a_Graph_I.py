from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        Return whether two indices belong to the same connected component.

        Idea:
        - Adjacent positions i and i-1 are connected if nums[i] - nums[i-1] <= maxDiff.
        - Build component ids in one pass.
        - For each query, answer True if both nodes have the same component id.
        """
        component = [-1] * n
        compId = 0
        component[0] = compId

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                compId += 1
            component[i] = compId

        res = []
        for u, v in queries:
            res.append(component[u] == component[v])

        return res


# Test cases inside the code
sol = Solution()

n1 = 5
nums1 = [1, 3, 6, 7, 10]
maxDiff1 = 2
queries1 = [[0, 1], [1, 2], [2, 4], [3, 4]]
print(sol.pathExistenceQueries(n1, nums1, maxDiff1, queries1))  # [True, False, False, True]

n2 = 4
nums2 = [1, 2, 4, 8]
maxDiff2 = 3
queries2 = [[0, 2], [1, 3], [0, 3]]
print(sol.pathExistenceQueries(n2, nums2, maxDiff2, queries2))  # [True, False, False]