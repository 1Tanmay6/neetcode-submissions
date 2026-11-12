class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
            
        count = 0
        slow = head
        fast = head
        nodes_to_be_rearranged = []
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            count += 1
        temp = slow
        slow = slow.next
        temp.next = None
        while slow is not None:
            nodes_to_be_rearranged.append(slow)
            slow = slow.next
        nodes_to_be_rearranged.reverse()
        prev = head
        curr = head.next
        for node in nodes_to_be_rearranged:
            prev.next = node
            node.next = curr
            prev = curr
            curr = curr.next