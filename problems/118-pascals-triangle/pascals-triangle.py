class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for n in range(1, numRows):
            row = [1]
            for m in range(n-1):
                row.append(result[n-1][m]+result[n-1][m+1])
            row.append(1)
            result.append(row)
            
        return result
