class Solution:
    def clearDigits(self, s: str) -> str:
        #create an empty stack 
        stack = []

        #loop through each character
        for cahr in s:
            #if digit remove last letter from stack
            if cahr.isdigit():
                if stack:
                    stack.pop()
        #if letter add to stack
            else:
                stack.append(cahr)

                #join all in stack and make final string
        return ''.join(stack)
    