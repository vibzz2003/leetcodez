# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        List1 = []
        curr = head
        while curr:
            List1.append(curr.val)
            curr = curr.next
        
        List1[left-1 : right] = List1[left-1 : right][::-1]

        new_head = ListNode(List1[0])
        curr = new_head
        for val in List1[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        
        return new_head

 