class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums)<=1:
            return 0
        
        #Radix Sort를 통한 정렬
        buckets = [deque() for _ in range(10)]
        queue = deque(nums)
        max_num = max(nums)
        factor=1
        
        while max_num>=factor:
            while queue:
                num = queue.popleft()
                buckets[num//factor%10].append(num)
            
            for bucket in buckets:
                while bucket:
                    queue.append(bucket.popleft())
            
            factor *=10
        nums=list(queue)
        
        #인접 두개 요소 간 차이 계산
        l,ans=0,(nums[1]-nums[0])
        while l<len(nums)-1:
            ans = max(nums[l+1]-nums[l],ans)
            l+=1
        return ans