class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        longest = max([len(x) for x in nums], default=0)
        a=[x*(10) for x in nums]
        print(a)
        nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)