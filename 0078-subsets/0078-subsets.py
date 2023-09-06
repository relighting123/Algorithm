class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,n=[],2**len(nums)
        for i in range(n):
            subans=[]
            for j in range(len(nums)):
                print(i,j)
                if (i >> j) & 1:
                    subans.append(nums[j])
            ans.append(subans)
        return ans
        
    