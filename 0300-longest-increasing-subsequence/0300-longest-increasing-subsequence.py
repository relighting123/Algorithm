class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        left = 0
        right = 1
        while right < n:
            if nums[right] > nums[left]:
                dp[right] = max(dp[right], dp[left] + 1)
            left += 1
            if left == right:
                left = 0
                right += 1
        return max(dp)