class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQueue = []
        ans = []
        for i in range(0, len(nums)):
            while maxQueue and nums[maxQueue[-1]]<nums[i]:
                maxQueue.pop(-1)
            maxQueue.append(i)
            if i>=k-1:
                if maxQueue[0]==i-k: maxQueue.pop(0)
                ans.append(nums[maxQueue[0]])
        return ans
            