# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1->2->3->4->5 = stack(5,4,3,2,1) = list[5,4,3,2,1]/5->4->3->2->1 = reverse again
        # or
        #1->2->3->4->5 = list[1,2,3,4,5] = reverse[list] = list[5,4,3,2,1] = operation
        # if n == 0 or head is None:
        #     return head

        # list1 = []

        # curr = head
        # while curr:
        #     list1.append(curr.val)
        #     curr = curr.next

        # #reverse
        # reversedlist = list1[::-1]

        # if n <= len(reversedlist):
        #     reversedlist.pop(n-1)

        # list2 = reversedlist[::-1]

        # if not list2:
        #     return None

        # dummy = ListNode(0)
        # curr = dummy
        # for val in list2:
        #     curr.next = ListNode(val)
        #     curr = curr.next
        
        # return dummy.next

        if not head or n == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
