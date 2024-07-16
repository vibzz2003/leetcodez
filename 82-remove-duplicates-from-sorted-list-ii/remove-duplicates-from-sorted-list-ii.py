# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:    
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            
            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next
            
            curr = curr.next

        return dummy.next