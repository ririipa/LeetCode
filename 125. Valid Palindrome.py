class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ""
        for char in s:
            if char.isalnum():
                alphanumeric += char.lower()

        return alphanumeric == alphanumeric[::-1]
    
    