# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None

        answer= []    
        point=head
        target = head
        while n>0:
            target = target.next
            n-=1
            
        if target is None:
            return head.next
        while target.next:
            answer.append(point)
            point=point.next
           
            target=target.next
        if len(answer)<1:
            answer.append(point)
        
        point.next=point.next.next    
        return answer[0]
        
        
        
        
        