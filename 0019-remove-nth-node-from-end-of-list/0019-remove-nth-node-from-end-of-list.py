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
        #target이 None인 경우라면 n==노드의 길이. 즉 최초 노드를 제거해야 하는 순간을 의미하므로 head.next를 return함.   
        if target is None:
            return head.next
        #target의 next가 None인 경우라면 최초 노드의 next를 제거해야 하는 경우 
        if target.next is None:
            head.next=head.next.next
            return head
            
        while target.next:
            answer.append(point)
            point=point.next
           
            target=target.next
        
        point.next=point.next.next    
        return answer[0]
        
        
        
        
        