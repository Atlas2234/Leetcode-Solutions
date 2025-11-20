"""
Time Complexity: O(M * N) where M is number of rows and N is number of columns in the grid
Space Complexity: O(M * N) in worst case for the recursion stack since it can go as deep as number of cells in the grid
"""
from rpds import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])

        visit = set()

        # Count of sub islands
        counter = 0

        def dfs(i, j):
            # Base case
            if i >= rows or j >= cols or i < 0 or j < 0 or grid2[i][j] == 0:
                return True
            # Already visited cell
            if (i, j) in visit:
                return True
            
            # Mark cell as visited
            visit.add((i, j))

            #Explore all 4 directions
            #Doing it this way to avoid short circuit since we want to traverse the entire island and mark it down as visited already
            bool1 = grid1[i][j] == 1
            bool2 = dfs(i, j + 1)
            bool3 = dfs(i + 1, j)
            bool4 = dfs(i, j - 1)
            bool5 = dfs(i - 1, j)
            return  bool1 and bool2 and bool3 and bool4 and bool5

        for i in range(rows):
            for j in range(cols):
                # If it's a land cell and not visited, perform DFS to check if it's a sub-island
                if grid2[i][j] == 1 and (i, j) not in visit and dfs(i, j):
                    # Increment sub-island count
                    counter += 1
        
        return counter
