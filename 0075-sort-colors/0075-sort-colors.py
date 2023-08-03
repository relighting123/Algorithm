from bisect import bisect_left,bisect_right
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,a,b=0,0,len(nums)-1    
        #속도 개선(불필요한 Swap 최소화)
        
        max_val,min_val = max(nums),min(nums)
        i=bisect_left(nums,min_val)
        a=i
        b=bisect_right(nums,max_val)-1
        
        print(a,b)
        
        
        while(i<=b):
            if nums[i]==0:
               # print("k",i)
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
                i+=1
                #print(nums)                
            elif nums[i]==2:
                nums[b],nums[i]=nums[i],nums[b]                
                b-=1            
            else:
                i+=1
            
            
    

            
    
        
        