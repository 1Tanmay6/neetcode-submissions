# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        counter = 0
        elements = {}

        while pointer is not None:
            elements[counter] = pointer
            counter += 1
            pointer = pointer.next

        target_index = len(elements) - n

        if target_index == 0:
            head = head.next
        else:
            prev = elements[target_index - 1]
            curr = elements[target_index]
            prev.next = curr.next

        return head