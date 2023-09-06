class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        # 비트마스킹을 이용하여 부분집합 생성
        for i in range(2**n):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            ans.append(subset)
        
        return ans
