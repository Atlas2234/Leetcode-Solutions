"""
Time Complexity: O(M * N) where M is the number of rows and N is the number of columns in the grid.
Space Complexity: O(M * N) in worst case for the recursion stack since it can go as deep as number of cells in the grid
"""

from rpds import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get grid dimensions
        rows = len(grid)
        cols = len(grid[0])

        # Track visited cells
        visited = set()

        # Count of islands
        count = 0

        # DFS to explore the island
        def dfs(i, j):
            # Base cases
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] == "0":
                return
            # Already visited cell
            if (i, j) in visited:
                return
            
            # Mark cell as visited
            visited.add((i, j))
            
            # Explore all four directions
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:                   
                    # Start DFS to mark all cells in this island as visited
                    dfs(i, j)
                    # Increment island count
                    count += 1
        # Return the total number of islands found
        return count

            