class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for p in s:
            if p in set(['(', '{', '[']):
                stack.append(p)
            else:
                if not stack or stack.pop() != pairs[p]:
                    return False
        
        if stack:
            return False
        return True


