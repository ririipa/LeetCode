class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in brackets:
                top_element = stack.pop() if stack else '#'
                if brackets[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack