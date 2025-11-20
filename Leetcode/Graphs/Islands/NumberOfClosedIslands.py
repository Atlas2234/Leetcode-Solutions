"""
Time Complexity: O(m * n) where m is number of rows and n is number of columns in grid
Space Complexity: O(m * n) in worst case for recursion stack since it can go as deep as number of cells in the grid
"""
from rpds import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        numIslands = 0

        # DFS over each island
        def dfs(i, j):

            # Base Case
            if i >= rows or j >= cols or i < 0 or j < 0:
                return False
            
            if grid[i][j] == 1 or (i, j) in visited:
                return True

            # Add coordinates of cell so we do not visit it again
            visited.add((i, j))

            # Check 4 directions of cell
            isClosed1 = dfs(i, j + 1)
            isClosed2 = dfs(i + 1, j)
            isClosed3 = dfs(i, j - 1) 
            isClosed4 = dfs(i - 1, j)
            
            return isClosed1 and isClosed2 and isClosed3 and isClosed4

        # Iterate through each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If cell is land and not visited, perform DFS
                if (i,j) not in visited and grid[i][j] == 0 and dfs(i, j):
                    numIslands += 1
        
        return numIslands