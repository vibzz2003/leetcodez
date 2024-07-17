# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k ==0 or head is None:
            return head

        list1 =[]
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next

        k = k%len(list1)
        rotated = list1[-k:] + list1[:-k]

        dummy = ListNode(0)
        curr = dummy
        for val in rotated:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next