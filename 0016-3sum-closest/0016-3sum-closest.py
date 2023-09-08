class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=0
        diffval=float("inf")
        nums.sort()
        def solveTwoPointer(i):
            nonlocal ans,diffval
            n=len(nums)
            l,r=i+1,n-1
            if l>=n:
                return

            while l<r:

                sumval=nums[i]+nums[l]+nums[r]
                #print("i",i,"l",l,"r",r,sumval,diffval,ans)
                if sumval<target:
                    l+=1
                    if abs(sumval-target)<diffval:
                        diffval=abs(sumval-target)
                        ans = sumval
                    
                elif sumval==target:
                    diffval = abs(sumval-target)
                    ans=sumval
                    return ans
                else:
                    r-=1
                    if abs(sumval-target)<diffval:
                        diffval=abs(sumval-target)
                        ans = sumval
                    
            return ans
        n=len(nums)
        for i in range(n-2):
            ans = solveTwoPointer(i)
        
        return ans
            
                    
