"""
Time Complexity: O(n + m) where n is size of nums1 and m is size of nums2
Space Complexity: O(n + m) for hashsets where n is size of nums1 and m is size of nums2
"""
from ast import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Answers
        answer1 = 0
        answer2 = 0

        # Hashsets to check if number exists in other list
        nums1Set = set()
        nums2Set = set()

        # Create hashsets - O(n + m) space where n is size of nums1 and m is size of nums2
        for n in nums1:
            nums1Set.add(n)
        
        for n in nums2:
            nums2Set.add(n)

        # Loop through nums1, check against nums2 - O(n + m) time
        for n in nums1:
            if n in nums2Set:
                answer1 += 1

        for n in nums2:
            if n in nums1Set:
                answer2 += 1 
        
        return [answer1, answer2]