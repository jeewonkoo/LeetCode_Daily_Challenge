# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next and n == 1: return None
        
        curr = head 
        cnt = 0
        back = None 
        
        while curr:
            if cnt == n: 
                back = head 
                break 
            curr = curr.next
            cnt += 1
    
        if back == None: 
            head = head.next 
            return head 
        
        while curr.next:
            curr = curr.next
            back = back.next
        
        back.next = back.next.next
            
        return head 