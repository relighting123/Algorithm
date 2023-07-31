class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        a[1]=nums[0]
        b=[1]*len(nums)
        b[-2]=nums[-1]
        for i in range(2,len(nums)):
            a[i]=a[i-1]*nums[i-1]
        
        for i in range(len(nums)-3,-1,-1):
            b[i]=b[i+1]*nums[i+1]
        return [a * b for a,b in zip(a,b)]