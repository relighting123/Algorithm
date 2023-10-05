class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if groupSize ==1:
            return True
        if n%groupSize != 0:
            return False
        
        l,r,visited,cnt =0,0,[False]*n,1
        visited[l]=True
        
        hand.sort()
        prevVal=hand[l]
        #print("정렬된 hand",hand)
        while max(l,r)<n:
            #print("before",hand[l],hand[r],l,r,prevVal,visited,cnt)
            if visited[r] or hand[r]==prevVal or r==l: 
                #print("r은 이미 방문했거나 이전 값과 동일 값입니다. 위치 +1합니다.")
                if r==l:
                    prevVal=hand[l]
                r+=1

                continue
            if hand[r]>prevVal+1 and prevVal!=-1:
                #print("현재 그룹 내 찾은 수는 ",cnt,"입니다", "groupsize 도달 전 연속 수가 아니므로 False 처리합니다")
                return False
            
            visited[l],visited[r]=True,True
            prevVal=hand[r]
            r+=1
            cnt+=1
            if all(visited) and cnt==groupSize:
                #print("return True")
                return True
            if cnt==groupSize:
                #print("get",visited)
                cnt,prevVal=1,-1
                while visited[l]:
                    l+=1
                visited[l]=True
                r=l
            #print("after 다음 경로 안내입니다",hand[l],hand[r],prevVal,visited,cnt)
        return True if cnt==groupSize else False    
