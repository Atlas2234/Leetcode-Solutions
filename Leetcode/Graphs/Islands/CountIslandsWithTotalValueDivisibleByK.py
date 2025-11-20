"""
Time Complexity: O(m*n) where m is number of rows and n is number of columns in the grid
Space Complexity: O(m*n) in worst case for the recursion stack since it can go as deep as number of cells in the grid
"""
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        # Track visited cells
        visit = set()

        # Count of islands with total value divisible by k
        islandCount = 0

        # Get grid dimensions
        rows = len(grid)
        cols = len(grid[0])

        # DFS to explore the island and calculate total value
        def dfs(i, j):
            # Base cases
            # Out of bounds or water cell
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == 0:
                return 0
            
            # Already visited cell
            if (i, j) in visit:
                return 0
            
            # Mark cell as visited
            visit.add((i, j))

            # Explore all four directions and accumulate total value
            total = grid[i][j] + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

            return total
        
        # Iterate through each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If it's a land cell and not visited, perform DFS to get total value of the island
                # and check if it's divisible by k
                if grid[i][j] > 0 and (i, j) not in visit and dfs(i, j) % k == 0:
                    # Increment island count
                    islandCount += 1
        # Return the count of islands with total value divisible by k
        return islandCount