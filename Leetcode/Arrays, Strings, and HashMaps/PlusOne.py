"""
Time Complexity: O(n) because we may need to traverse the entire digits array in the worst case (e.g., when all digits are 9).
Space Complexity: O(1) because we are modifying the input array in place, except for the case where we need to add an additional digit at the front, which is still considered O(1) additional space.
Trick: Start from the last digit and handle the carry as you would in elementary addition. Then at the end, if there's still a carry, insert it at the front of the array.
"""

from rpds import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Initialize last index of digits array
        index = len(digits) - 1

        # Initialize first and last digits of a sum
        first = 1
        last = 0

        # Loop through the digits array
        while index >= 0:

            # Calculate the sum
            sum = digits[index] + first

            # If sum < 10 modify then replace the current value with the sum
            if sum < 10:
                digits[index] = sum
                return digits
            
            # If sum > 10 get first and last digit
            if sum >= 10:
                first = sum // 10
                second = sum % 10
                digits[index] = second

            index = index - 1
        
        # If loop ends without returning then we know that the first index value's sum is greater than 10
        # Insert the first digit into the front of the array
        digits.insert(0, first)

        return digits