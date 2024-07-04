# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        carry = 0

        while l1 != None or l2 != None or carry != 0:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + carry
            digit = sum%10
            carry = sum // 10


            new_node = ListNode(digit)

            if not head:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head