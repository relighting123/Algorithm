
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if groupSize ==1: return True
        if n%groupSize != 0: return False
        
        l,r,visited,cnt =0,0,[True]+[False]*(n-1),1
        hand.sort()
        prevVal=hand[l]
        while r<n:
            if visited[r] or hand[r] == prevVal: 
                r += 1;
                continue
            if hand[r]>prevVal+1 and r!=l: return False
            
            visited[l],visited[r],prevVal=True,True,hand[r]            
            r+=1
            cnt+=1
            if cnt==groupSize:
                if all(visited) : return True
              
                while visited[l]: l+=1
                visited[l]=True
                r=l
                cnt,prevVal=1,hand[l]
        return True if cnt==groupSize else False 