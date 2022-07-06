from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(1)
    """

    def generate(self, num_rows: int) -> List[List[int]]:
        pascal = []

        for level in range(1, num_rows + 1):
            row = [1] * level
            for i in range(1, level - 1):
                row[i] = pascal[level - 2][i - 1] + pascal[level - 2][i]
            pascal.append(row)

        return pascal
