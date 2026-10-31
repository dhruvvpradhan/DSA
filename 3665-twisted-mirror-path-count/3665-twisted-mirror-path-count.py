class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Two possible first moves from (0, 0)
        right[0][1] = 1
        down[1][0] = 1

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    # Empty cell
                    ways = (right[i][j] + down[i][j]) % MOD

                    # Move right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + ways
                        ) % MOD

                    # Move down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + ways
                        ) % MOD

                else:
                    # Mirror cell

                    # Right becomes down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    # Down becomes right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % MOD

