# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None:
            return head

        list1 = []
        curr = head

        while curr:
            list1.append(curr.val)
            curr = curr.next

        n = len(list1)
        i = 0
        while i+k<=n:
            list1[i: i+k] = list1[i:i+k][::-1]
            i+=k
        
        dummy = ListNode(list1[0])
        curr = dummy
        for val in list1[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy