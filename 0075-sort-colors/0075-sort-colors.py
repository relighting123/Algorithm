from bisect import bisect_left,bisect_right
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,a,b=0,0,len(nums)-1    

        while(i<=b):
            if nums[i]==0  and i > a:
               # print("k",i)
                nums[a],nums[i]=nums[i],nums[a]
                a+=1
                #print(nums)                
            elif nums[i]==2  and i < b:
                nums[b],nums[i]=nums[i],nums[b]                
                b-=1            
            else:
                i+=1
            
            
    

            
    
        
        