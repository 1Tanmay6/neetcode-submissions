# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1: str = None
        num_2: str = None
        final_ll: ListNode = None
        final_ll_curr: ListNode = None

        while l1 is not None:
            if not num_1:
                num_1 = str(l1.val)
            else:
                tmp_num_1 = "%d%s" % (l1.val, num_1)
                num_1 = tmp_num_1
            l1 = l1.next
        
        while l2 is not None:
            if not num_2:
                num_2 = str(l2.val)
            else:
                tmp_num_2 = "%d%s" % (l2.val, num_2)
                num_2 = tmp_num_2
            l2 = l2.next
        
        num = str(int(num_1) + int(num_2))
        for ele in num[::-1]:
            if final_ll is None:
                final_ll = ListNode(val=int(ele))
                final_ll_curr = final_ll
            else:
                final_ll_curr.next = ListNode(val=int(ele))
                final_ll_curr = final_ll_curr.next
        
        return final_ll
