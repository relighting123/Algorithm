class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None

        answer= []    
        point=head
        target = head

        #찾아야할 간격만큼 target을 설정.
        while n>0:
            target = target.next
            n-=1
        #1) target이 None인 경우라면 n==노드의 길이. 즉 최초 노드를 제거해야 하는 순간을 의미하므로 head.next를 return함.   
        if target is None:
            return head.next
        #2) target의 next가 None인 경우라면 최초 노드의 next를 제거해야 하는 경우 이미로 head.next를 head.next.next로 연결하여 기존의 head.next를 삭제함.
        if target.next is None:
            head.next=head.next.next
            return head
        
        #3) 이외의 경우에 대해 target의 next가 None이 될때까지 수행하여 삭제해야 할 포인트 이전까지 멈춤. 단 최초의 point 값을 별도로 저장하고 이후에 point 값은 update해나감.
        while target.next:
            if len(answer)<1: answer.append(point) 
            point=point.next            
            target=target.next
            
        #삭제해야 할 포인트 이전 지점에서 2번 케이스와 동일하게 그 다음 노드와 연결하도록 하여 삭제시킴.
        point.next=point.next.next    
        return answer[0]
        
        
        
        
        