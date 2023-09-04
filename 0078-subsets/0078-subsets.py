from typing import List
from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        
        def backtrack(start, current_subset):
            subsets.append(current_subset[:])  # 현재 부분 집합을 결과에 추가
            
            for i in range(start, n):
                current_subset.append(nums[i])  # 요소를 현재 부분 집합에 추가
                backtrack(i + 1, current_subset)  # 다음 요소를 선택하도록 재귀 호출
                current_subset.pop()  # 현재 요소를 제거하여 다른 조합을 시도
        
        backtrack(0, [])
        return subsets
