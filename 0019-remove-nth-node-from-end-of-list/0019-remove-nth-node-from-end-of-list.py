# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        if head.next.next == None:
            if n==2:
                return head.next
            else :
                head.next=None
                return head
        answer= []
        
        dummy = ListNode(0)
        dummy.next = head
        point=dummy
        target = dummy
        while n>0:
            target = target.next
            n-=1
        
        while target.next:
            answer.append(point)
            point=point.next
            target=target.next
        if len(answer)<1:
            answer.append(point)

        point.next=point.next.next
        return answer[0].next
        
        
        
        
        