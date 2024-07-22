class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmp = [[name, height] for name, height in zip(names, heights)]
        tmp.sort(key=lambda e: e[1], reverse=True)
        return [e[0] for e in tmp]