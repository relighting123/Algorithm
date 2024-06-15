class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            if nums[left]>nums[right]:
                left+=1
            else:
                right-=1
        #print(left,right)
        
        return nums[left]