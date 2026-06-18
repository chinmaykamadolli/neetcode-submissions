class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CtO = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in CtO:
                if stack and stack[-1] == CtO[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        return True if not stack else False