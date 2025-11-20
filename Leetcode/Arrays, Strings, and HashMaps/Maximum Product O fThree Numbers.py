"""
Time Complexity: O(n) because we traverse the list once and sorting the small and large lists takes constant time.
Space Complexity: O(1) because we are using a fixed amount of space.
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Find the two smallest and three largest numbers
        smallestTwo = [float('inf')]*2
        # Find the three largest numbers
        largestThree = [float('-inf')]*3
        # Iterate through the array to find required numbers
        for num in nums:
            # Update smallest two
            if num <= smallestTwo[0]:
                smallestTwo[0] = num
                # Keep the smallestTwo sorted
                smallestTwo.sort(reverse=True)
            # Update largest three
            if num >= largestThree[0]:
                largestThree[0] = num
                # Keep the largestThree sorted
                largestThree.sort()

        # Calculate the maximum product of three numbers
        return max(smallestTwo[0]*smallestTwo[1]*largestThree[2], 
                   largestThree[0]*largestThree[1]*largestThree[2])
    
"""
Alternate solution
Time Complexity: O(n) because we traverse the list twice.
Space Complexity: O(1) because we are using a fixed amount of space.
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        small = [float('inf')] * 2
        large = [float('-inf')] * 3

        # Find the 2 smallest numbers in nums
        for n in nums:
            if n < small[0]:
                small[1] = small[0]
                small[0] = n
            elif n >= small[0] and n < small[1]:
                small[1] = n
        
        # Find the 3 largest numbers in nums
        for n in nums:
            if n > large[2]:
                large[0] = large[1]
                large[1] = large[2]
                large[2] = n

            elif n <= large[2] and n > large[1]:
                large[0] = large[1]
                large[1] = n

            elif n <= large[1] and n > large[0]:
                large[0] = n
        
        # Calculate product of the two smallest digits
        smallestProd = small[0] * small[1]

        return max(large[0] * large[1] * large[2], large[2] * smallestProd)