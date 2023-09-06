class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,n=[],2**len(nums)
        for partial_combination in range(n):
            subans=[]
            for j in range(len(nums)):
                if j>partial_combination:
                    continue
                if partial_combination&1<<j :
                    subans.append(nums[j])
            ans.append(subans)
        return ans