from collections import Counter


class Solution:
    """
    Time:   O(max(n, m))
    Memory: O(1)
    """

    def isAnagram(self, first: str, second: str) -> bool:
        return Counter(first) == Counter(second)
