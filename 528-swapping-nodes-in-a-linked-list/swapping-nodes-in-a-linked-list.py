# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        List = []
        while head!= None:
            List.append(head.val)
            head = head.next
        
        List[k-1], List[len(List)-k] = List[len(List)-k], List[k-1]

        print(List)
        head = None
        current = None

        for num in List:
            new_node = ListNode(num)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
        current = head

        return head
        