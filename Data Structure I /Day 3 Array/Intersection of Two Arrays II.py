from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n + m)
    Memory: O(n + m)
    """

    def intersect(self, first: List[int], second: List[int]) -> List[int]:
        common = Counter(first) & Counter(second)
        return sum(([num] * cnt for num, cnt in common.items()), [])


class Solution:
    """
    Time:   O(nlog(n) + mlog(m))
    Memory: O(1)
    """

    def intersect(self, first: List[int], second: List[int]) -> List[int]:
        first.sort()
        second.sort()

        i = j = 0
        intersection = []

        while i < len(first) and j < len(second):
            if first[i] == second[j]:
                intersection.append(first[i])
                i += 1
                j += 1
            elif first[i] < second[j]:
                i += 1
            else:
                j += 1

        return intersection
