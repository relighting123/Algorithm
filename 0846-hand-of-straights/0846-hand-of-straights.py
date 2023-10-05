class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if groupSize ==1:
            return True
        if n%groupSize != 0:
            return False
        
        dic=defaultdict(int)
        hand.sort()
       
        for i in range(n):
            dic[hand[i]]+=1
        cnt=0
        while cnt<n:
            if cnt==n:
                return True
            for i in dic:
                if dic[i]>0:
                    s=i
                    break
            for i in range(groupSize):
                if dic[s+i]==0:
                    return False
                dic[s+i]-=1
                cnt+=1
        return True
            
                
        