class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 연구자가 쓴 i번째 논문의 인용수
        # 3개의 논문이 최소 3개의 인용을 가짐..
        citations.sort(reverse=True)
        return max(map(min, enumerate(citations, start=1)))