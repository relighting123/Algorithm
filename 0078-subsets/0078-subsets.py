
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans,n=[[]],2**len(nums)
        for i in range(n):
            subans=[]
            for j in range(min(i,len(nums))):
                print(i,j)
                if i&(1<<j) :
                    subans.append(nums[j])
                if subans not in ans:
                    ans.append(subans)
        return ans