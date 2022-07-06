from collections import Counter


class Solution:
    """
    Time:   O(max(n, m))
    Memory: O(1)
    """

    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        return not Counter(ransom_note) - Counter(magazine)
