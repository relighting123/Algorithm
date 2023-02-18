class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer= [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            j=0
            while(j<i):
                if(nums[j]<nums[i]):
                    answer[i]=max(answer[j]+1,answer[i])                                                     
          
                j+=1
      
        return max(answer)
        