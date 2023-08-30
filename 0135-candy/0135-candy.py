class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        nums = [1]*N
        
        for n in range(1, N):
            if ratings[n-1] < ratings[n]:
                nums[n] = nums[n-1] + 1
        
        for n in range(N-1, 0, -1):
            if ratings[n-1] > ratings[n]:
                nums[n-1] = max(nums[n-1], nums[n] + 1)
                
        return sum(nums)