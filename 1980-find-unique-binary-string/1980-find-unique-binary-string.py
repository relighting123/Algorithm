class Solution(object):
    def findDifferentBinaryString(self, nums):
        dic_decimal=dict(zip([int(str(num),2) for num in nums],[0]*len(nums)))
        return next(bin(n)[2:].zfill(len(nums)) for n in range(2 ** len(nums) + 1) if n not in dic_decimal)
                        
    
                
        