class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,n=[],2**len(nums)
        for i in range(n):
            subans=[]
            for j in range(min(i,len(nums))):
                if i&1<<j :
                    subans.append(nums[j])
            ans.append(subans)
        return ans