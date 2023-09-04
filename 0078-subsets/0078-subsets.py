class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]

        n=len(nums)
        def dfs(start,subans):
            ans.append(subans)
            for i in range(1,len(nums)):
                if start+i>=len(nums):
                    break
                dfs(start+i,subans+[nums[start+i]])
            
        for i in range(len(nums)):
            dfs(i,[nums[i]])
        return ans

        