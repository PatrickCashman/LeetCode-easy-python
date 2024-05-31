from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        # Continue loop while current is not null
        while current:
            # While the next node exists and has the same value as the current node, delete the duplicate
            while current.next and current.next.val == current.val:
                # Skip the duplicate node by pointing to the next of next node
                current.next = current.next.next
            # Move to the next node
            current = current.next
        return head

#time: O(n)
#space: O(1)

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)


my_solution = Solution()
result_head = my_solution.deleteDuplicates(head)

result = []
while result_head:
    result.append(result_head.val)
    result_head = result_head.next
print(result)