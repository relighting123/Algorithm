class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        rightmax=float("-inf")
        leftmin=float("inf")
        lmin=[0]*len(nums)
        rmax=[0]*len(nums)
        for i in range(len(nums)):
            leftmin=min(leftmin,nums[i])
            lmin[i]=leftmin
        for i in range(len(nums)):
            rightmax=max(rightmax,nums[len(nums)-1-i])
            rmax[len(nums)-1-i]=rightmax
        for i in range(len(nums)):
            if lmin[i]<nums[i]<rmax[i]:
                return True
        return False
            