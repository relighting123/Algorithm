class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if groupSize ==1:  return True
        if n%groupSize != 0:  return False
        
        l,r,visited,cnt =0,0,[True]+[False]*(n-1),1
        
        hand.sort()
        prevVal=hand[l]
        while r<n:
            if visited[r] or hand[r]==prevVal or r==l: 
                if r==l:
                    prevVal=hand[l]
                r+=1
                continue
            if hand[r]>prevVal+1 and prevVal!=-1:
                return False
            
            visited[l],visited[r]=True,True
            prevVal=hand[r]
            r+=1
            cnt+=1
            if cnt==groupSize:
                if all(visited) : return True
                #print("get",visited)
                cnt,prevVal=1,-1
                while visited[l]:
                    l+=1
                visited[l]=True
                r=l
            #print("after 다음 경로 안내입니다",hand[l],hand[r],prevVal,visited,cnt)
        return True if cnt==groupSize else False    
