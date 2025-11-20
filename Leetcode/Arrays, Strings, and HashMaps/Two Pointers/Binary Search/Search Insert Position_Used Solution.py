'''
Time Complexity: O(log n) because we are performing binary search.
Space Complexity: O(1) because we are using a fixed amount of space.

Trick: Use binary search to find the correct index to insert the target. Then account for edge cases where the target is less than the smallest element or greater than the largest element.

Used Solution: Binary Search notes. Need to redo this problem later to solidify understanding.
'''
from rpds import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Set pointers
        left = 0
        right = len(nums) - 1

        # Initialize possible index for insertion
        possibleIndex = 0

        # Perform binary search
        while left <= right:

            # Get middle index
            mid = (left + right) // 2

            # Compare value in mid with target
            if nums[mid] == target:
                return mid
            # Adjust pointers based on comparison
            if nums[mid] < target:
                left = mid + 1
                # Update possible index
                possibleIndex = mid + 1
            else:
                right = mid - 1
                # Update possible index. Doing mid instead of mid - 1 to handle edge case where target is less than the smallest element.
                # When we insert, we will always insert to the right of mid when nums[mid] > target.
                possibleIndex = mid

        # Return the possible index where the target should be inserted
        # Handle edge case where target is less than the smallest element
        if possibleIndex < 0:
            return 0
        # Handle edge case where target is greater than the largest element
        elif possibleIndex > len(nums) - 1:
            return len(nums)
        # Normal case
        else:
            return possibleIndex