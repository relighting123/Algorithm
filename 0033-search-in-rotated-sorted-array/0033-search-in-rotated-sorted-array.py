from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r= 0,n-1
        if n==0:
            return -1
        if l>=r-1:
            if target != min(nums) and target != max(nums):
                return -1
            else :
                return 0 if target==nums[0] else 1
        
        
        while l < r-1:
            
            if nums[l]<nums[r]:
                r=0
                break
            mid = (l + r) // 2
            
            if nums[mid]>nums[r]:
                l=mid
            else :
                r=mid
      
        t = nums[r:]+nums[:r]
        
        idx=bisect_left(t,target)
        #print(r,idx,t)
        if idx>=n or t[idx] != target :
            return -1
        
        return (idx + r)%n
            