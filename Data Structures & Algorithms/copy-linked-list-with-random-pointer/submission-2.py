"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        pos_counter = 0
        new_head: Optional[Node]
        curr: Optional[Node]
        oll_pointer = head
        oll_lookup = {}
        new_ll_lookup = {}

        # 1. Create the lookups and new singly linked list
        while oll_pointer is not None:
            oll_lookup[oll_pointer] = {
                "rand": oll_pointer.random,
                "pos": pos_counter
            }

            new_ll_lookup[pos_counter] = Node(x = oll_pointer.val)

            pos_counter += 1
            oll_pointer = oll_pointer.next

        # 2. Re-init the oll_pointer = head 
        oll_pointer = head
        pos_counter = 0

        # 3. Create a loop to build our new SLL
        for pos, node in new_ll_lookup.items():
            if pos == 0:
                new_head = node
                curr = new_head
            else:
                curr.next = node
                curr = curr.next
        
        curr = new_head
        
        # 4. We use the lookups to map back to random elements
        while oll_pointer is not None and curr is not None:
            # find the old node using the lookup
            rand_node = oll_lookup[oll_pointer]["rand"]
            if rand_node == None:
                curr.random = None
            else:
                rand_node_pos = oll_lookup[rand_node]["pos"]
                # we will use the rand pos to complete the current node of the new LL
                new_ll_rand_node = new_ll_lookup[rand_node_pos]
                curr.random = new_ll_rand_node
            curr = curr.next
            oll_pointer = oll_pointer.next

        # 4. Return the new_head
        return new_head
                

