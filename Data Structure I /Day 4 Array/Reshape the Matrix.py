from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        if r * c != n * m:
            return matrix
        return [[matrix[(row * c + col) // m][(row * c + col) % m] for col in range(c)] for row in range(r)]
