"""
Time Complexity: O(N) where N is the length of the string s, this is because we traverse the string once to extract words and once more to build the final string.
Space Complexity: O(N) for storing words in a list, this is because in the worst case, all characters in the string are part of words (no spaces).

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # List to store words
        stringList = []

        # Final answer
        ans = ""
        
        # Extract words from string
        i = 0
        # Two pointer approach
        while i < len(s):
            # If not space, extract word
            if s[i] != " ":
                j = i
                tempStr = ""
                # Extract until space or end of string
                while j < len(s) and s[j] != " ":
                    tempStr = tempStr + s[j]
                    j += 1
                stringList.append(tempStr)
                i = j
            i += 1
        
        # Build answer string in reverse order
        for i in range(len(stringList) - 1, -1, -1):
            print(i)
            ans = ans + stringList[i] + " "
        
        ans = ans.strip()

        # Return the final answer
        return ans
    

"""
Time Complexity: O(N) where N is the length of the string s, this is because we traverse the string once to split it into words and once more to join them in reverse order.
Space Complexity: O(N) for storing words in a list, this is because in the worst case, all characters in the string are part of words (no spaces).

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        # List to store words
        a = []
        # Split string into words
        s = s.split()
        # Append words in reverse order
        for v in range(len(s)-1,-1,-1):
            a.append(s[v])
        # Join the reversed words into a single string
        return " ".join(a)