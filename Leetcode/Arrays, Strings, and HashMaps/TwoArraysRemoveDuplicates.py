"""
Given two integer arrays num1 and num2, return two arrays answer where answer[0] is a list of all distinct integers 
in num1 which are not present in num2, and answer[1] is a list of all distinct integers in num2 which are not present in num1.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""
from typing import List

class Solution:
    def TwoArraysRemoveDuplicate(self, num1: List[int], num2: List[int]) -> List[List[int]]:
        
        # Initialize sets to store unique elements
        num1Set = set()
        num2Set = set()

        # Initialize new arrays as the answer
        noDupe1 = []
        noDupe2 = []

        # Add elements into the set
        for n in num1:
            num1Set.add(n)
        
        for n in num2:
            num2Set.add(n)

        # Loop through each array and create new arrays without duplicates
        for n in num1:
            if n not in num2Set:
                noDupe1.append(n)
                
        for n in num2:
            if n not in num1Set:
                noDupe2.append(n)
        
        return [noDupe1, noDupe2]


    '''
    1. Create 2 sets to store the unique elements of each array.
    2. Loop through each array and compare each element with the set of the other array.
    3. Add each element to a new array. If the element is in the set, do not add that element.
    '''

    """
    Test Cases
    """
if __name__ == "__main__":
    sol = Solution()
    num1 = [1, 2, 3, 3]
    num2 = [2, 4, 6, 6]
    answer = sol.TwoArraysRemoveDuplicate(num1, num2)
    print(answer[0], answer[1]) # Should print [[1, 3, 3], [4, 6, 6]]

    num1 = [1, 2, 3, 3]
    num2 = []
    answer = sol.TwoArraysRemoveDuplicate(num1, num2)
    print(answer[0], answer[1]) # Should print [[1, 2, 3, 3], []]

    num1 = [1, 2, 3, 3]
    num2 = [2, 3]
    answer = sol.TwoArraysRemoveDuplicate(num1, num2)
    print(answer[0], answer[1]) # Should print [[1], []]