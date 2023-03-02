class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        dic_decimal={}
        dic_decimal=dict(zip([int(str(num),2) for num in nums],[0]*len(nums)))
        for n in range(2**len(nums)+1):
            if n not in dic_decimal:
                return bin(n)[2:].zfill(len(nums))
                
                        
    
                
        