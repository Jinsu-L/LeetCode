class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        output = []
        candidate = []
        for row in matrix:
            min_idx = -1
            min_value = float("inf")
            for i, e in enumerate(row):
                if min_value > e:
                    min_value = e
                    min_idx = i

            candidate.append(min_idx)

        for i, j in enumerate(candidate):
            max_idx = -1
            max_value = float("-inf")
            for k in range(len(candidate)):
                if matrix[k][j] > max_value:
                    max_idx = k
                    max_value = matrix[k][j]

            if i == max_idx:
                output.append(matrix[i][j])

        return output



        