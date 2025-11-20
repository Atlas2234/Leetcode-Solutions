"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        
        currentMon = 1
        nextDay = 1

        total = 0
        for i in range(n):
            if i >= 7 and i % 7 == 0:
                currentMon += 1
                nextDay = currentMon + 1
                total += currentMon
            else:
                total += nextDay
                nextDay = nextDay + 1
        
        return total
    
"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        # number of complete weeks
        k = n // 7
        # first and last term of arithmetic series
        F = 28
        # last term
        L = 28 + (k - 1) * 7
        # sum of arithmetic series
        arithmetic_sum = k * (F + L) // 2
        
        # sum of remaining days
        monday = 1 + k
        # last term
        final_week = 0
        # number of remaining days
        for day in range(n % 7):
            # last term
            final_week += monday + day
        # total sum
        return arithmetic_sum + final_week