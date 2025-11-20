"""
Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m * n) in the worst case for the recursion stack and visited set
"""
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Track visited cells
        visit = set()

        def dfs(i, j):
            # Base cases
            # Out of bounds or water cell
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j]==0:
                return 1
            # Already visited cell
            if (i, j) in visit:
                return 0
            
            # Mark cell as visited
            visit.add((i, j))
            # Explore all four directions
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)

            # Return the perimeter count for this cell
            return perim
        
        # Start DFS from the first land cell found
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

"""
Similar solution replaces the visited set with in-place modification of the grid. Complexities are the same.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(i, j):
            # Base cases
            # Out of bounds or water cell
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j]==0:
                return 1
            # Already visited cell
            if grid[i][j] == -1:
                return 0
            
            # Mark cell as visited
            grid[i][j] = -1
            # Explore all four directions
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)

            # Return the perimeter count for this cell
            return perim
        
        # Start DFS from the first land cell found
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i, j)

"""
Space Optimized Solution without DFS
Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(1) since no extra space is used.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # Initialize perimeter count
        ans = 0

        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # Check if the cell is land
                if grid[row][col] == 1:
                    ans += 4
                    # Check for adjacent land cells to subtract shared edges
                    # Check upper cell for shared edge subtraction
                    if row > 0 and grid[row-1][col] == 1:
                        ans -= 2
                    # Check left cell for shared edge subtraction
                    if col > 0 and grid[row][col-1] == 1:
                        ans -=2
        
        return ans