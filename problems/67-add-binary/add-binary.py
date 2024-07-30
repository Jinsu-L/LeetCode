from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        results = []
        for left, right in zip_longest(reversed(a), reversed(b)):
            add = carry
            if left:
                add += int(left)
            if right:
                add += int(right)

            print(add)
            if add > 1:
                carry = 1 
                results.append(add % 2)
            else:
                carry = 0
                results.append(add)
    
        if carry:
            results.append(1)
        
        return "".join(list(map(str, reversed(results))))