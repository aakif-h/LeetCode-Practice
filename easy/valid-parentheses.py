class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        brackets = {')':'(',
                    ']':'[',
                    '}':'{'}
        
        for bracket in s:
            if bracket in brackets:
                closing = stack.pop() if stack else 'EMPTY'
                if brackets[bracket] != closing:
                    return False
            else:
                stack.append(bracket)
        return not stack
