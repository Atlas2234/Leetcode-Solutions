"""
Time Complexity: O(m*n) where m is number of rows and n is number of columns in the grid
Space Complexity: O(m*n) in worst case for the recursion stack since it can go as deep as number of cells in the grid
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # Track maximum area found
        currMax = 0
        def dfs(i, j):
            # Base cases
            # Out of bounds or water cell
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j]==0 or grid[i][j] == -1:
                return 0

            # Mark cell as visited
            grid[i][j] = -1

            # Explore all four directions
            area = 1 + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

            # Return the area for this cell
            return area
        
        # Start DFS from the first land cell found
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # Update maximum area found
                    currMax = max(currMax, dfs(i,j))
        
        return currMax
    
"""
Alternative solution using a visited set instead of in-place modification of the grid
Time Complexity: O(m*n) where m is number of rows and n is number of columns in the grid
Space Complexity: O(m*n) in worst case for the recursion stack since it can go as deep as number of cells in the grid
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i, j):
            # Base cases
            # Out of bounds or water cell
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j]==0:
                return 0
            # Already visited cell
            if (i, j) in visit:
                return 0

            # Mark cell as visited
            visit.add((i, j))

            # Explore all four directions
            area = 1 + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

            # Return the area for this cell
            return area

        # Start DFS from the first land cell found
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    # Update maximum area found
                    currMax = max(currMax, dfs(i, j))

        return currMax